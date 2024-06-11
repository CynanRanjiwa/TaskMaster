// creating a login page 
import React from 'react';
import AuthForm from '../components/authForm';

const Login = () => {
    const handleLogin  = (data) => {
        // handle the login logic 
        console.log('Login data:', data);
    }

    };
    return (
        <AuthForm type="login" onSubmit={handleLogin} />
    );
    

    
    export default Login;