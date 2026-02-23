import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function CheckOut(){

    let [products,setProducts]=useState([]);
    let [customers,setCustomers]=useState([]);

    let [orders,setOrders]=useState({
        "product":"",
        "customer":"",
        "price":"",
        "quantity":"",
        "created_at":""
    })

    let[order,setOrder]=useState([]);

    useEffect(()=>{
        axios.get("http://127.0.0.1:8000/products/").then((res)=>{setProducts(res.data)}).catch((error)=>{alert(error.message)});

        axios.get("http://127.0.0.1:8000/customers/").then((res)=>{setCustomers(res.data)}).catch((error)=>{alert(error.message)});

        getData();
    },[]);

    function getData(e){
        axios.get("http://127.0.0.1:8000/orders/").then((res)=>{setOrder(res.data)}).catch((error)=>{alert(error.message)});
    }

    function updateInput(e){
        setOrders({
            ...orders,
            [e.target.name]:e.target.value,
        })
    }

    function safe(e){
        e.preventDefault();
        axios.post("http://127.0.0.1:8000/orders/",orders).then(()=>{
            getData();
            setOrders({
                "product":"",
                "customer":"",
                "price":"",
                "quantity":"",
                "created_at":""
            })
        }).catch((error)=>{console.log(error.response.data);});
    }

    return (
      <React.Fragment>
        <section>
          <div className="container mt-4">
            <div className="row justify-content-center">
              <div className="col-md-5">
                <div className="card">
                  <div className="card-header bg-success text-white">
                    <h1 className="text-center">Orders</h1>
                  </div>
                  <div className="card-body">
                    <form action="" onSubmit={safe}>
                      <div className="form-group">
                        <select name="product" id="" value={orders.product} onChange={updateInput} className="form-control">
                          <option value="">Select Product</option>
                          {
                            products.map((p)=>{
                                return(
                                    <option key={p.id} value={p.id}>
                                    {p.name}
                                </option>
                                )
                            })
                          }
                        </select>
                      </div>
                      <div className="form-group">
                        <select name="customer" id="" value={orders.customer} onChange={updateInput} className="form-control">
                          <option value="">Select Customer</option>
                          {
                            customers.map((c)=>{
                                return(
                                    <option key={c.id} value={c.id}>
                                    {c.cname}
                                </option>
                                )
                            })
                          }
                        </select>
                      </div>
                      <div className="form-group">
                        <input type="text" name="price" id="" value={orders.price} onChange={updateInput} placeholder="Enter Price" className="form-control" />
                      </div>
                      <div className="form-group">
                        <input type="text" name="quantity" id="" value={orders.quantity} onChange={updateInput} placeholder="Enter Quantity" className="form-control" />
                      </div>
                      <div className="form-group">
                        <input type="date" name="created_at" id="" value={orders.created_at} onChange={updateInput} className="form-control" />
                      </div>

                      <button className="btn btn-outline-success">Order</button>
                      <Link to='/' className="btn btn-outline-secondary float-right">BACK</Link>

                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section>
            <div className="container mt-4">
                {
                    order.length > 0 ?
                    <table className="table table-bordered table-striped table-hover text-center">
                        <thead className="bg-success text-white">
                            <tr>
                                <th>ID</th>
                                <th>Product</th>
                                <th>Customer</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Date</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                order.map((o)=>{
                                    return(
                                        <tr key={o.id}>
                                            <td>{o.id}</td>
                                            <td>{o.product_name}</td>
                                            <td>{o.customer_name}</td>
                                            <td>{o.price}</td>
                                            <td>{o.quantity}</td>
                                            <td>{o.created_at}</td>
                                            <td>
                                                <i className="fa fa-eye mr-3 text-warning" ></i>
                                                <i className="fa fa-pencil mr-3 text-success" ></i>
                                                <i className="fa fa-trash text-danger" ></i>
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
    );
}