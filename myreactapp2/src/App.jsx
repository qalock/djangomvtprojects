import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import EmployeeList from "./components/EmployeeList";
import AddEmployee from "./components/AddEmployee";
import FindEmployee from "./components/FindEmployee";
import EditEmployee from "./components/EditEmployee";

export default function App() {
  return (
    <React.Fragment>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<EmployeeList />} />
          <Route path="/add" element={ <AddEmployee/> } />
          <Route path="/find/:id" element={ <FindEmployee/> } />
          <Route path="/edit/:id" element={ <EditEmployee/> } />
        </Routes>
      </BrowserRouter>
    </React.Fragment>
  );
}
