const formulario = document.getElementById("formulario");
const listaProdutos = document.getElementById("listaProdutos");
const busca = document.getElementById("busca");

const produtos = [
    {
        id: 1,
        nome: "chinelo quadradis",
        preco: 20,
        imagem: "./img/bob.jpg",
        descricao: "Chinelo quadradis",
        categoria: "ropa",
        estoque: 3,
        status: "Ativo",
        
    },
        
    {   
        id: 2, 
        nome: "Miojo",
        preco: 5,
        imagem: "/img/miojo.jpg",
        descricao: "O classic miojis né",
        categoria: "Comida",
        estoque: 5,
        status: "Ativo",
    },

    {   
        id: 3,
        nome:  "Jarra",
        preco: 15,
        imagem: "/img/jarra.jpg",
        descricao: "É uma jarra",
        categoria: "Objeto",
        estoque: 20,
        status: "Ativo",
    },
 
    {
        id: 4,
        nome:  "Camisa do space jam",
        preco: 30,
        imagem: "/img/spacejam.jpg",
        descricao: "Essa camisa é boladex e vale a pena comprar",
        categoria: "Roupa",
        estoque: 0,
        status: "Desligado",
    },    

    {
        id: 5,
        nome: "Mangá de bleach",
        preco: 10,
        imagem: "/img/bleach.jpg",
        descricao: "Esse anime é bolado",
        categoria: "Livro",
        estoque: 50 ,
        status: "Ativo",        
    }
];

function mostrarProdutos(lista) {

    listaProdutos.innerHTML = ""; 

lista.forEach(produto => {
    listaProdutos.innerHTML += `
    
    <div class="card h-100">
   <img src="${produto.imagem}" class="card-img-top" alt="${produto.nome}">
        <div class="card-body">
            <h5 class="card-title">${produto.nome}</h5>

            <h4 class="text-success">

            ${produto.preco.toLocaleString("pt-BR", {style: "currency",currency: "BRL"})}</h4>

            <p class="card-text">${produto.descricao}</p>

            <p><strong>Categoria:</strong> ${produto.categoria}</p>

            <p><strong>Estoque:</strong> ${produto.estoque}</p>

            <p><strong>Status:</strong> ${produto.status}</p>

            <a href="#" class="btn btn-primary">
                Comprar
            </a>

            <button 
                class="btn btn-warning"
                onclick="editarProduto(${produto.id})">
                Editar
                </button>

                <button 
                class="btn btn-danger"
                onclick="excluirProduto(${produto.id})">
                Excluir
                </button>

  </div>
</div>
`;
});
}

function atualizarResumo(){

document.getElementById("totalProdutos").textContent = produtos.length;

    const ativos = produtos.filter(produto => produto.status === "Ativo");
    document.getElementById("produtosAtivos").textContent = ativos.length;

    const valorTotal = produtos.reduce((total, produto) => {
        return total + produto.preco;
    }, 0);

    document.getElementById("valorTotal").textContent =
        valorTotal.toLocaleString("pt-BR", {
            style: "currency",
            currency: "BRL"
        });
}

function excluirProduto(id){

const indice = produtos.findIndex(produto => produto.id === id);

    if (indice !== -1) {

        produtos.splice(indice, 1);

        mostrarProdutos(produtos);

        atualizarResumo();

    }
}

function editarProduto(id){

const produto = produtos.find(produto => produto.id === id);

    document.getElementById("nome").value = produto.nome;
    document.getElementById("preco").value = produto.preco;
    document.getElementById("imagem").value = produto.imagem;
    document.getElementById("descricao").value = produto.descricao;
    document.getElementById("categoria").value = produto.categoria;
    document.getElementById("estoque").value = produto.estoque;
    document.getElementById("status").value = produto.status;   
}

formulario.addEventListener("submit", (event) => {
        event.preventDefault();

        console.log("Formulario enviado");

        const nome = document.getElementById("nome").value;
        const preco = parseFloat(document.getElementById("preco").value);
        const imagem = document.getElementById("imagem").value;
        const descricao = document.getElementById("descricao").value;
        const categoria = document.getElementById("categoria").value;
        const estoque = document.getElementById("estoque").value;
        const status = document.getElementById("status").value;



        const novoProduto = {
            id: Date.now(),
            nome: nome,
            preco: preco,
            imagem: imagem,
            descricao: descricao,
            categoria: categoria,
            estoque: estoque,
            status: status
        };

        produtos.push(novoProduto);
        atualizarResumo();
        formulario.reset();
        console.log(produtos);
        mostrarProdutos(produtos);
        alert("Sucesso ao cadastrar")
    });

      mostrarProdutos(produtos);
      atualizarResumo();

      busca.addEventListener("input", () => {

    const texto = busca.value.toLowerCase();

    const filtrados = produtos.filter(produto =>
        produto.nome.toLowerCase().includes(texto)
    );

    mostrarProdutos(filtrados);


});
