import React, { useEffect, useState } from "react";
import axios from 'axios'
import { Link } from "react-router-dom";

export default function EmployeeList(){
    
  const [employee, setEmployee] = useState([]);

  useEffect(() => {
    getData();
  }, []);

  function getData(){
     axios.get("http://localhost:9000/employees")
      .then((res) => {
        setEmployee(res.data);
      })
      .catch((error) => {
        alert(error.message);
      });
  }

  function del(id){
    axios.delete("http://localhost:9000/employees/"+id).then(()=>{alert("Record Deleted Successfully")
        getData()
    }).catch((error)=>{alert(error.message)})
  }

  return (
    <React.Fragment>
      <div className="container">
        <p className="h1 text-center text-secondary">Employee List</p>

        <section>
          <Link to="/add" className="btn btn-primary btn-sm">
            ADD
          </Link>
        </section>

        <section>
          {
            employee.length > 0 ? (
              <table className="table table-bordered table-striped table-hover">
                <thead>
                  <tr className="bg-info text-white text-center">
                    <th>Employee ID</th>
                    <th>Employee Name</th>
                    <th>Employee Salary</th>
                    <th>Employee Email</th>
                    <th>Employee Image</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                    {
                        employee.map((emp)=>{
                            return(
                                <tr key={emp.id}>
                                    <td>{emp.id}</td>
                                    <td>{emp.name}</td>
                                    <td>{emp.salary}</td>
                                    <td>{emp.email}</td>
                                    <td>
                                        <img src={emp.image} className="img-fluid" style={{width:250,height:150}}></img>
                                    </td>
                                    <td>
                                        <Link to={`/find/${emp.id}`} className="fa fa-eye mr-3 text-info"></Link>
                                        <Link to={`/edit/${emp.id}`} className="fa fa-pencil text-success mr-3"></Link>
                                        <i className="fa fa-trash text-danger" onClick={()=>{del(emp.id)}} ></i>
                                    </td>
                                </tr>
                            )
                        })
                    }
                 
                    
                </tbody>
              </table>
            ) : (
              <p className="h2 text-danger text-center">
                Records Not Found
              </p>
            )
          }
        </section>
      </div>
    </React.Fragment>
  );
}