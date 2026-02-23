import axios from "axios";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";

export default function FindEmployee() {
  let { id } = useParams();
  let [employee, setEmployee] = useState({});

  useEffect(() => {
    axios
      .get(`http://localhost:9000/employees/${id}`)
      .then((res) => {
        setEmployee(res.data);
      })
      .catch((error) => {
        alert(error.message);
      });
  }, []);

  function updateInput(e){
        setEmployee({
            ...employee,
            [e.target.name]:e.target.value
        })
    }

  return (
    <React.Fragment>
      <div className="row justify-content-center">
        <div className="col-md-7">
          <div className="card">
            <div className="card-header bg-primary text-white">
              <h1 className="text-center">Show Employee</h1>
            </div>
            <div className="card-body">
                <div className="row">
                  <div className="col-md-6">
                    <img src={employee.image} alt="" className="img-fluid"  />
                  </div>
                  <div className="col-md-6">
                    <ul className="list-group">
                      <li className="list-group-item">
                        <h4>Employee ID: {employee.id}</h4>
                      </li>
                      <li className="list-group-item">
                        <h4>Employee Name: {employee.name}</h4>
                      </li>
                      <li className="list-group-item">
                        <h4>Employee Email: {employee.email}</h4>
                      </li>
                      <li className="list-group-item">
                        <h4>Employee Salary: {employee.salary}</h4>
                      </li>
                    </ul>
                  </div>
                </div>
                <div className="card-footer text-center">
                  <Link to='/' className="btn btn-outline-info" >Back</Link>
                </div>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}
