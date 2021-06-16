import React from 'react'

import Home from './Home'
import NotFound from './NotFound'
import Fruits from './Fruits'
import Baskets from './Baskets'

import '../sass/main.sass'

const routes = {
    "" : { level : 0, component : Home },
    "home" : { level : 0, component : Home },
    "baskets" : { level : 1, component : Baskets },
    "fruits" : { level : 1, component : Fruits } 
}

const Router = () => {
    let location = window.document.location.pathname.split('/')

    console.log(location)

    for ( let i in routes )
        if ( i === location[1] )
            return React.createElement(routes[i].component, null, null)

    return React.createElement(NotFound, null, null)
};

export default Router