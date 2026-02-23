import React from "react";
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import AddEmployee from "./components/AddEmployee";
import Employee_list from "./components/employee_list";
import EditEmployee from "./components/EditEmployee";
import FindEmployee from "./components/FindEmployee";

export default function App(){
  return(
    <>
      <p className="h1 text-center text-danger">Hello World</p>

      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Employee_list/> } />
        <Route path="/add" element={ <AddEmployee/>} />
        <Route path="/edit" element={ <EditEmployee/>} />
        <Route path="/find" element={ <FindEmployee/>} />

      </Routes>
      </BrowserRouter>

    </>
  )
}