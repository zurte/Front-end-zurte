const produtos = [
    {
        nome: "chinelo quadradis",
        preco: "$20,00",
        imagem: "fsdfdssff",
        descricao: "Chinelo quadradis",
        
    },
        
    {    
        nome: "Miojo",
        preco: "$5,00",
        imagem: "fsfdssdf",
        descricao: "O classic miojis né",
    },

    {
        nome:  "Jarra",
        preco: "$15,00",
        imagem: "fdsfssdf",
        descricao: "É uma jarra",
    },
 
    {
        nome:  "Camisa do space jam",
        preco: "$30,00",
        imagem: "sdfsdfsdf",
        descricao: "Essa camisa é boladex e vale a pena comprar",
    },    

    {
        nome: "Mangá de bleach",
        preco: "$10,00",
        imagem: "sdfsdfe",
        descricao: "Esse anime é bolado",
    }
];
const listaProdutos = document.getElementById("listaProdutos");

produtos.forEach(produtos => {
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

console.log("JS carregado!");
