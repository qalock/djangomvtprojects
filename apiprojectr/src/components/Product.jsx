import React, { useEffect, useState } from "react";
import axios from 'axios';
import { Link } from "react-router-dom";

export default function Product(){

    let[product,setProduct]=useState({
        "name":"",
        "price":"",
        "quantity":"",
        "image":"",
    });

    let[products,setProducts]=useState([]);

    useEffect(()=>{
        getData();
    },[]);

    function getData(){
        axios.get("http://127.0.0.1:8000/products/").then((res)=>{setProducts(res.data)}).catch((error)=>{alert(error)});
    }
    

    function updateInput(e){
        setProduct({
            ...product,
            [e.target.name]:e.target.value,
        })
    }

    function safe(e){
        e.preventDefault();
        axios.post("http://127.0.0.1:8000/products/",product).then(()=>{
            getData();
            setProduct({
              name: "",
              price: "",
              quantity: "",
              image: "",
            });}
        ).catch((error)=>{alert(error)});
    }
    

    return(
        <React.Fragment>
            <section>
                <div className="container mb-5 text-center">
                    <Link to='/add_customer' className="btn btn-outline-secondary btn-sm"  >Customer</Link>
                    <Link to='/orders' className="btn btn-outline-success btn-sm" >Orders</Link>
                </div>
            </section>
            <section>
                <div className="container">
                    <div className="row justify-content-center">
                        <div className="col-md-5">
                            <div className="card">
                                <div className="card-header bg-info text-white">
                                    <h1 className="text-center" >Add Product</h1>
                                </div>
                                <div className="card-body">
                                    <form action="" onSubmit={safe}>
                                        <div className="form-group">
                                            <input type="text" name="name" id="" value={product.name} onChange={updateInput} placeholder="Enter Product Name" className="form-control" />
                                        </div>
                                        <div className="form-group">
                                            <input type="text" name="price" id="" value={product.price} onChange={updateInput} placeholder="Enter Product Price" className="form-control" />
                                        </div>
                                        <div className="form-group">
                                            <input type="text" name="quantity" id="" value={product.quantity} onChange={updateInput} placeholder="Enter Product Qunatity" className="form-control" />
                                        </div>
                                        <div className="form-group">
                                            <input type="text" name="image" id="" value={product.image} onChange={updateInput} placeholder="Enter Product Image Url" className="form-control" />
                                        </div>
                                        <button className="btn btn-outline-info">ADD</button>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <section>
                <div className="container mt-5">
                    {
                        products.length > 0 ?
                        <table className="table table-bordered table-striped table-hover text-center">
                            <thead className="bg-secondary text-white">
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>Price</th>
                                    <th>Qunatity</th>
                                    <th>Image</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    products.map((p)=>{
                                        return(
                                            <tr key={p.id} >
                                                <td>{p.id}</td>
                                                <td>{p.name}</td>
                                                <td>{p.price}</td>
                                                <td>{p.quantity}</td>
                                                <td>
                                                    <img src={p.image} alt="" height={150} />
                                                </td>
                                                <td>
                                                    <i className="fa fa-eye mr-3 text-warning"></i>
                                                    <i className="fa fa-pencil mr-3 text-success"></i>
                                                    <i className="fa fa-trash  text-danger"></i>
                                                </td>
                                            </tr>
                                        )
                                    })
                                }
                            </tbody>
                        </table>
                        :
                        <p className="h1 text-center text-danger">Record Not Found</p>
                    }
                </div>
            </section>
        </React.Fragment>
    )
}