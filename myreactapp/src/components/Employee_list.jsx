import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

function EmployeeList() {

  const [employee, setEmployee] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:9000/employees")
      .then((res) => {
        setEmployee(res.data);
      })
      .catch((error) => {
        alert(error.message);
      });
  }, []);

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
                                <tr>
                                    <td>{emp.id}</td>
                                    <td>{emp.ename}</td>
                                    <td>{emp.esal}</td>
                                    <td>{emp.email}</td>
                                    <td>
                                        <img src={emp.eimage} className="img-fluid" style={{width:250,height:150}}></img>
                                    </td>
                                    <td>
                                        <Link to={"/find"} className="mr-3">Find</Link>
                                        <Link to={"/edit"} className="mr-3">Edit</Link>
                                        <Link to={"/delete"}>Delete</Link>
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

export default EmployeeList;