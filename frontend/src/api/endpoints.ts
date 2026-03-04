import { apiClient } from './client';
import { LoginPayload, RegisterPayload } from '../types';
export const login = (payload: LoginPayload) => apiClient.post('/login', payload);
export const register = (payload: RegisterPayload) => apiClient.post('/register', payload);
export const logout = () => apiClient.post('/logout');
