var addToCartBtn = document.getElementsByClassName('addToCart')


for(var i=0; i < addToCartBtn.length; i++){
    addToCartBtn[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        console.log(`productId: ${productId}, action: ${action}`)
        console.log('User', user)

        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            console.log('User is logged in, sending data...')
        } 
    })
}


