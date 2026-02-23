import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link,useNavigate } from "react-router-dom";


export default function AddEmployee(){
    const[employee,setEmployee]=useState({
         "name":"",
         "salary":"",
         "email":"",
         "image":""
    })

    const navigate=useNavigate();


    function updateInput(e){
        setEmployee({
            ...employee,
            [e.target.name]:e.target.value
        })
    }

    function safe(e){
        e.preventDefault()
        axios.post("http://localhost:9000/employees",employee).then(()=>{alert("Record Added successfully");
            navigate('/')
         }).catch((error)=>{alert(error.message)})
    }

  return(
    <React.Fragment>
      <div className="row justify-content-center">
        <div className="col-md-4">
            <div className="card">
                <div className="card-header bg-info text-white">
                    <h1 className="text-center">Add Employee</h1>
                </div>
                <div className="card-body ">
                    <form action="" onSubmit={safe} >
                        <div className="form-group">
                            <input type="text" name="name" placeholder="Enter Employee Name" id="" value={employee.name} onChange={updateInput} className="form-control" />
                        </div>
                        <div className="form-group">
                            <input type="text" name="salary" placeholder="Enter Employee Salary" id="" value={employee.salary} onChange={updateInput} className="form-control" />
                        </div>
                        <div className="form-group">
                            <input type="text" name="email" placeholder="Enter Employee Email" id="" value={employee.email} onChange={updateInput} className="form-control" />
                        </div>
                        <div className="form-group">
                            <input type="text" name="image" placeholder="Enter Employee Image" id="" value={employee.image} onChange={updateInput} className="form-control" />
                        </div>
                        <button className="btn btn-outline-info">Add</button>
                        <Link to='/' className="btn btn-outline-primary float-right" >Back</Link>
                    </form>
                </div>
            </div>
        </div>
      </div>
    </React.Fragment>
  )
}