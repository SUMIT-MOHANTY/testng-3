import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
const Login: React.FC = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const formik = useFormik({
    initialValues: { email: '', password: '' },
    validationSchema: Yup.object({
      email: Yup.string().email().required(),
      password: Yup.string().required()
    }),
    onSubmit: async (values, { setSubmitting, setErrors }) => {
      try {
        await login(values);
        navigate('/dashboard');
      } catch (e:any) {
        setErrors({ email: 'Invalid credentials' });
      }
      setSubmitting(false);
    }
  });
  return (
    <form onSubmit={formik.handleSubmit}>
      <div><input name="email" placeholder="Email" {...formik.getFieldProps('email')} /></div>
      {formik.touched.email && formik.errors.email ? <div>{formik.errors.email}</div> : null}
      <div><input type="password" name="password" placeholder="Password" {...formik.getFieldProps('password')} /></div>
      {formik.touched.password && formik.errors.password ? <div>{formik.errors.password}</div> : null}
      <button type="submit" disabled={formik.isSubmitting}>Login</button>
    </form>
  );
};
export default Login;
