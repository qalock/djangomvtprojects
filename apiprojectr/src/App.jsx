import React from "react";
import {BrowserRouter , Routes, Route} from 'react-router-dom'
import Product from "./components/Product";
import Customer from "./components/Customer";
import CheckOut from "./components/CheckOut";

export default function App(){
  return(
    <React.Fragment>
      <BrowserRouter>
      <Routes>
        <Route path="/" element={ <Product/> } />
        <Route path="/add_customer" element={ <Customer/> } />
        <Route path="/orders" element={ <CheckOut/> } />
      </Routes>
      </BrowserRouter>
    </React.Fragment>
  )
}