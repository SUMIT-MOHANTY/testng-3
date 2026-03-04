import axiosInstance from '../../utils/axiosInstance';

export const getPolicy = async (policyId: string) => {
  const response = await axiosInstance.get(`/api/policies/${policyId}`);
  return response.data;
};
