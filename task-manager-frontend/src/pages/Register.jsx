import React from 'react';
import AuthForm from '../components/AuthForm';

const Register = () => {
  const handleRegister = (data) => {
    // Handle registration logic (e.g., API call)
    console.log('Register data:', data);
  };

  return <AuthForm type="register" onSubmit={handleRegister} />;
};

export default Register;