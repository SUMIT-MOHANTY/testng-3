import axiosInstance from '../../utils/axiosInstance';

export const getPremium = async (policyId: string) => {
  const response = await axiosInstance.get(`/api/premiums/${policyId}`);
  return response.data;
};

export const subscribePremiumUpdates = (url: string, handler: (data: any) => void) => {
  const ws = new WebSocket(url);
  ws.onmessage = e => { const data = JSON.parse(e.data); handler(data); };
  ws.onerror = err => console.error('WS error', err);
  return () => ws.close();
};
