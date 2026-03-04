import React, { createContext, useContext, useState, ReactNode } from 'react';
import * as api from '../api/endpoints';
export interface AuthContextProps {
  user: string | null;
  isAuthenticated: boolean;
  login: (payload: any) => Promise<void>;
  register: (payload: any) => Promise<void>;
  logout: () => Promise<void>;
}
const AuthContext = createContext<AuthContextProps | undefined>(undefined);
export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<string | null>(null);
  const isAuthenticated = !!user;
  const login = async (payload: any) => {
    const res = await api.login(payload);
    if (res.status === 200) setUser(payload.email);
  };
  const register = async (payload: any) => {
    await api.register(payload);
    await login({ email: payload.email, password: payload.password });
  };
  const logout = async () => {
    await api.logout();
    setUser(null);
  };
  return (
    <AuthContext.Provider value={{ user, isAuthenticated, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
};
