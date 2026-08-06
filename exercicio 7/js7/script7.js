const formulario = document.getElementById("formulario");
const listaProdutos = document.getElementById("listaProdutos");

const produtos = [
    {
        nome: "chinelo quadradis",
        preco: 20,
        imagem: "./img/bob.jpg",
        descricao: "Chinelo quadradis",
        categoria: "ropa",
        estoque: 3,
        status: "Ativo",
        
    },
        
    {    
        nome: "Miojo",
        preco: 5,
        imagem: "/img/Miojo.jpg",
        descricao: "O classic miojis né",
        categoria: "Comida",
        estoque: 5,
        status: "Ativo",
    },

    {
        nome:  "Jarra",
        preco: 15,
        imagem: "/img/A jarra.jpg",
        descricao: "É uma jarra",
        categoria: "Objeto",
        estoque: 20,
        status: "Ativo",
    },
 
    {
        nome:  "Camisa do space jam",
        preco: 30,
        imagem: "/img/spacejam.jpg",
        descricao: "Essa camisa é boladex e vale a pena comprar",
        categoria: "Roupa",
        estoque: 0,
        status: "Desligado",
    },    

    {
        nome: "Mangá de bleach",
        preco: 10,
        imagem: "/img/Bleach_vol._01.jpg",
        descricao: "Esse anime é bolado",
        categoria: "Livro",
        estoque: 50 ,
        status: "Ativo",        
    }
];

function mostrarProdutos() {

    listaProdutos.innerHTML = ""; 

produtos.forEach(produto => {
    listaProdutos.innerHTML += `
    <div class="card" style="width: 18rem;">
  <img src="${produto.imagem}" class="card-img-top" alt="${produto.nome}">
  <div class="card-body">
    <h5 class="card-title">${produto.nome}</h5>
    <h4 class="card-text">${produto.preco.toLocaleString("pt-BR", {style: "currency", currency: "BRL" })}}</h4>
    <p class="card-text">${produto.descricao}</p>
    <p class="card-text">${produto.categoria}</p>
    <p class="card-text">${produto.estoque.toLocaleString("pt-BR", {style: "currency", currency: "BRL" })}}}</p>
    <p class="card-text">${produto.status}</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
`;
});
}

formulario.addEventListener("submit", (event) => {
        event.preventDefault();

        console.log("Formulario enviado");

        const nome = document.getElementById("nome").value;
        const preco = document.getElementById("preco").value;
        const imagem = document.getElementById("imagem").value;
        const descricao = document.getElementById("descricao").value;
        const categoria = document.getElementById("categoria").value;
        const estoque = document.getElementById("estoque").value;
        const status = document.getElementById("status").value;



        const novoProduto = {
            nome: nome,
            preco: preco,
            imagem: imagem,
            descricao: descricao,
            categoria: categoria,
            estoque: estoque,
            status: status
        };

        produtos.push(novoProduto);
        console.log(produtos);
        mostrarProdutos();
    });

      mostrarProdutos();
