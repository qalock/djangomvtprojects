import axios from "axios";
import React, { useEffect, useState } from "react";
import { useParams} from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";


export default function EditEmployee(){
  let {id}=useParams();
  let [employee,setEmployee]=useState({
    name: "",
    salary: "",
    email: "",
    image: ""
  });
  const navigate=useNavigate();

  useEffect(()=>{
    axios.get(`http://localhost:9000/employees/${id}`).then((res)=>{setEmployee(res.data)}).catch((error)=>{alert(error.message)})
  },[id]);

  function updateInput(e){
      setEmployee({
        ...employee,
        [e.target.name]:e.target.value,
      })
  }

  function safe(e){
    e.preventDefault();
    axios.put(`http://localhost:9000/employees/${employee.id}`,employee).then(()=>{
      alert("Record Updated Successfully")
      navigate('/')
    }).catch((error)=>{alert(error.message)})
  }

  return(
    <React.Fragment>
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <div className="card">
              <div className="card-header bg-secondary text-white">
                <h1 className="text-center">Edit Employee</h1>
              </div>
              <div className="card-body">
                <form action="" onSubmit={safe} >
                  <div className="form-group">
                    <input type="text" name="name" id="" value={employee.name} onChange={updateInput} className="form-control" placeholder="Enter Name" />
                  </div>
                  <div className="form-group">
                    <input type="text" name="salary" id="" value={employee.salary} onChange={updateInput} className="form-control" placeholder="Enter Salary" />
                  </div>
                  <div className="form-group">
                    <input type="text" name="email" id="" value={employee.email} onChange={updateInput} className="form-control" placeholder="Enter Email" />
                  </div>
                  <div className="form-group">
                    <input type="text" name="image" id="" value={employee.image} onChange={updateInput} className="form-control" placeholder="Enter Image url" />
                  </div>
                  <button className="btn btn-outline-secondary">Edit</button>
                  <Link to='/' className="btn btn-outline-warning float-right" >Back</Link>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  )
}