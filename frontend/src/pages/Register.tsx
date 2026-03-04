import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
const Register: React.FC = () => {
  const { register } = useAuth();
  const navigate = useNavigate();
  const formik = useFormik({
    initialValues: { email: '', password: '', confirmPassword: '' },
    validationSchema: Yup.object({
      email: Yup.string().email().required(),
      password: Yup.string().required(),
      confirmPassword: Yup.string().oneOf([Yup.ref('password'), null], 'Passwords must match').required()
    }),
    onSubmit: async (values, { setSubmitting, setErrors }) => {
      try {
        await register(values);
        navigate('/dashboard');
      } catch (e:any) {
        setErrors({ email: 'Registration failed' });
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
      <div><input type="password" name="confirmPassword" placeholder="Confirm Password" {...formik.getFieldProps('confirmPassword')} /></div>
      {formik.touched.confirmPassword && formik.errors.confirmPassword ? <div>{formik.errors.confirmPassword}</div> : null}
      <button type="submit" disabled={formik.isSubmitting}>Register</button>
    </form>
  );
};
export default Register;
