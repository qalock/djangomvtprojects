import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";


export default function AddEmployee(){
    let [employee,setEmployee]=useState({
        id:"",
        ename:"",
        esal:"",
        email:"",
        eimage:""

    })

    useEffect(()=>{
        getData()
    },[])

    function updateInput(e){
        setEmployee({
            ...employee,
            [e.target.name]:e.target.value
    })
    }

    function getData(){
        axios.post("http://localhost:9000/employees",employee).then(()=>{alert("Record Added Successfully")}).catch((error)=>{alert(error.message);});
    }


    return(
        <>
        <div className="row justify-content-center">
            <div className="col-md-5">
                <div className="card">
                    <div className="card-header bg-info text-white">
                        <h1 className="text-center">Add Employee</h1>
                    </div>
                    <div className="card-body">
                        <form action="" onSubmit={getData} >
                            <div className="form-group">
                                <input type="number" name="id" id="" value={employee.id} onChange={updateInput} placeholder="Enter Employee Id" className="form-control"/>
                            </div>
                            <div className="form-group">
                                <input type="text" name="ename" id="" value={employee.ename} onChange={updateInput} placeholder="Enter Employee Name" className="form-control"/>
                            </div>
                            <div className="form-group">
                                <input type="number" name="esal" id="" value={employee.esal} onChange={updateInput} placeholder="Enter Employee Salary" className="form-control"/>
                            </div>
                            <div className="form-group">
                                <input type="text" name="email" id="" value={employee.email} onChange={updateInput} placeholder="Enter Employee Email" className="form-control"/>
                            </div>
                            <div className="form-group">
                                <input type="text" name="eimage" id="" value={employee.eimage} onChange={updateInput} placeholder="Enter Employee Image Location" className="form-control"/>
                            </div>
                            <button className="btn btn-outline-info">Add</button>
                            <Link to='/' className="btn btn-outline-warning float-right">Back</Link>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}