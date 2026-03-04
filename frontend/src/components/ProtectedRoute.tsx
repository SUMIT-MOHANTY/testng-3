import React from 'react';
import { Navigate } from 'react-router-dom';
function ProtectedRoute({ children }: { children: JSX.Element }) {
  const isAuthenticated = false; // placeholder
  return isAuthenticated ? children : <Navigate to="/login" replace />;
}
export default ProtectedRoute;
