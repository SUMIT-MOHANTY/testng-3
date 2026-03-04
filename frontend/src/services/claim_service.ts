import axiosInstance from '../../utils/axiosInstance';

export const submitClaim = async (formData: FormData) => {
  const response = await axiosInstance.post('/api/claims', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data;
};
