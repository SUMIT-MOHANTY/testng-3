import React from 'react';
function Login() {
  const handleLogin = async () => {
    alert('Login flow would start here.');
  };
  return <button onClick={handleLogin}>Login with Azure AD B2C</button>;
}
export default Login;
