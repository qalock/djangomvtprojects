import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Customer(){

    let [customer,setCustomer]=useState({
        "cname":"",
        "caddress":"",
        "cphone":"",
        "cimage":""
    });

    let [customers,setCustomers]=useState([]);

    useEffect(()=>{
        getData();
    },[])

    function getData(){
        axios.get("http://127.0.0.1:8000/customers/").then((res)=>{ setCustomers(res.data)}).catch((error)=>{alert(error.message)});
    }

    function safe(e){
        e.preventDefault();
        axios.post("http://127.0.0.1:8000/customers/",customer).then(()=>{
            getData();
            setCustomer({
                "cname":"",
                "caddress":"",
                "cphone":"",
                "cimage":""
            })
        }).catch((error)=>{alert(error.message)});
    }

    function updateInput(e){
        setCustomer({
            ...customer,
            [e.target.name]:e.target.value,
        })
    }



    return(
        <React.Fragment>
            <section>
                <div className="container mt-4">
                    <div className="row justify-content-center">
                        <div className="col-md-5">
                            <div className="card">
                                <div className="card-header bg-warning text-white">
                                    <h1 className="text-center">ADD Customer</h1>
                                </div>
                                <div className="card-body">
                                    <form action="" onSubmit={safe} >
                                        <div className="form-group">
                                            <input type="text" name="cname" id="" value={customer.cname} onChange={updateInput} placeholder="Enter Customer name" className="form-control" />
                                        </div>
                                        <div className="form-group">
                                            <input type="text" name="caddress" id="" value={customer.caddress} onChange={updateInput} placeholder="Enter Customer Address" className="form-control" />
                                        </div>
                                        <div className="form-group">
                                            <input type="text" name="cphone" id="" value={customer.cphone} onChange={updateInput} placeholder="Enter Customer Phone" className="form-control" />
                                        </div>
                                        <div className="form-group">
                                            <input type="text" name="cimage" id="" value={customer.cimage} onChange={updateInput} placeholder="Enter Customer Image" className="form-control" />
                                        </div>
                                    <button className="btn btn-outline-warning" >ADD</button>
                                    <Link to='/' className='btn btn-outline-secondary float-right'  >Back</Link>
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
                        customers.length > 0 ?
                        <table className="table table-bordered table-striped table-hover text-center">
                            <thead className="bg-warning text-white">
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>Address</th>
                                    <th>Phone</th>
                                    <th>Image</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    customers.map((c)=>{
                                        return(
                                            <tr key={c.id}>
                                                <td>{c.id}</td>
                                                <td>{c.cname}</td>
                                                <td>{c.caddress}</td>
                                                <td>{c.cphone}</td>
                                                <td>
                                                    <img src={c.cimage} alt="" height={150} />
                                                </td>
                                                <td>
                                                    <i className="fa fa-eye mr-3 text-info"></i>
                                                    <i className="fa fa-pencil mr-3 text-success"></i>
                                                    <i className="fa fa-trash text-danger"></i>
                                                </td>
                                            </tr>
                                        )
                                    })
                                }
                            </tbody>

                        </table>
                        :
                        <p className="h1 text-center text-danger">Record Not found</p>
                    }
                </div>
            </section>
        </React.Fragment>
    )
}