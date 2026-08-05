const formulario = document.GetElementById("formCadastro")

formulario.addEventListener("submit", function (event) {
    event.preventDefault();

    console.log("Formulario enviado");

    const nome = document.GetElementById("nome").value;
    const preco = document.GetElementById("preco").value;
    const imagem = document.GetElementById("imagem").value;
    const descricao = document.GetElementById("descricao").value;
    const categoria = document.GetElementById("categoria").value;
    const estoque = document.GetElementById("estoque").value;
    const status = document.GetElementById("status").value;



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

const produtos = [
    {
        nome: "chinelo quadradis",
        preco: "$20,00",
        imagem: "fsdfdssff",
        descricao: "Chinelo quadradis",
        categoria: "",
        estoque: "",
        status: "",
        
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
const listaProdutos = document.GetElementById("listaProdutos");

function mostrarProdutos() {

    listaProdutos.innerHTML = ""; 

produtos.forEach(produto => {
    listaProdutos.innerHTML += `
    <div class="card" style="width: 18rem;">
  <img src="${produtos.imagem}" class="card-img-top" alt="${produtos.nome}">
  <div class="card-body">
    <h5 class="card-title">${produtos.nome}</h5>
    <p class="card-text">${produtos.descricao}</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
`;
});
}

mostrarProdutos();
