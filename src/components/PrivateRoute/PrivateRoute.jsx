import React from "react";
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ child }) => {
  const accessToken = localStorage.getItem("token") || null;
  return accessToken ? child : <Navigate to="/login" replace />;
};

export default PrivateRoute;
