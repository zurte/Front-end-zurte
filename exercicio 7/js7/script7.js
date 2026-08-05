const formulario = document.getElementById("formulario");

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

    });

      mostrarProdutos();

const produtos = [
    {
        nome: "chinelo quadradis",
        preco: "$20,00",
        imagem: "./img/bob.jpg",
        descricao: "Chinelo quadradis",
        categoria: "ropa",
        estoque: "3",
        status: "Ativo",
        
    },
        
    {    
        nome: "Miojo",
        preco: "$5,00",
        imagem: "fsfdssdf",
        descricao: "O classic miojis né",
        categoria: "",
        estoque: "",
        status: "",
    },

    {
        nome:  "Jarra",
        preco: "$15,00",
        imagem: "fdsfssdf",
        descricao: "É uma jarra",
        categoria: "",
        estoque: "",
        status: "",
    },
 
    {
        nome:  "Camisa do space jam",
        preco: "$30,00",
        imagem: "sdfsdfsdf",
        descricao: "Essa camisa é boladex e vale a pena comprar",
        categoria: "",
        estoque: "",
        status: "",
    },    

    {
        nome: "Mangá de bleach",
        preco: "$10,00",
        imagem: "sdfsdfe",
        descricao: "Esse anime é bolado",
        categoria: "",
        estoque: "",
        status: "",        
    }
];
const listaProdutos = document.getElementById("listaProdutos");

function mostrarProdutos() {

    listaProdutos.innerHTML = ""; 

produtos.forEach(produto => {
    listaProdutos.innerHTML += `
    <div class="card" style="width: 18rem;">
  <img src="${produto.imagem}" class="card-img-top" alt="${produto.nome}">
  <div class="card-body">
    <h5 class="card-title">${produto.nome}</h5>
    <h4 class="card-text">${produto.preco}</h4>
    <p class="card-text">${produto.descricao}</p>
    <p class="card-text">${produto.categoria}</p>
    <p class="card-text">${produto.estoque}</p>
    <p class="card-text">${produto.status}</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
`;
});
}


