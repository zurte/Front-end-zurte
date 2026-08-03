const produtos = [
    {
        nome: "chinelo quadradis"
        preco: "$20,00"
        Imagem: ""
        descricao: "Chinelo quadradis"
        
    },
        
    {    
        nome: "Miojo"
        preco: "$5,00"
        imagem:
        descricao: "O classic miojis né"
    },

    {
        nome:  "Jarra"
        preco: "$15,00"
        imagem:
        descricao: "É uma jarra"
    },
 
    {
        nome:  "Camisa do space jam"
        preco: "$30,00"
        imagem:
        descricao: "Essa camisa é boladex e vale a pena comprar"
    },    

    {
        nome: "Mangá de bleach"
        preco: "$10,00"
        imagem:
        descricao: "Esse anime é bolado"
    }
];
const catalogo = document.getElementById("catalogo");

produtos.forEach(produtos => {
    catalogo.innerHTML += `
    <div class="card" style="width: 18rem;">
  <img src="${produtos.imagem}..." class="card-img-top" alt="${produtos.nome}...">
  <div class="card-body">
    <h5 class="card-title">${produtos.nome}</h5>
    <p class="card-text">${produtos.descricao}</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
`;
});
