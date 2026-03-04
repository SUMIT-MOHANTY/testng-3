import React, { useEffect, useState } from 'react';
import { IPayment } from '../types';
import axiosInstance from '../utils/axiosInstance';

type Props = { policyId: string };
export const PaymentHistory: React.FC<Props> = ({ policyId }) => {
  const [payments, setPayments] = useState<IPayment[]>([]);
  useEffect(() => {
    axiosInstance.get('/api/payments', { params: { policyId } })
      .then(res => setPayments(res.data));
  }, [policyId]);
  const fmt = (n: number, cur: string) => new Intl.NumberFormat(undefined, { style: 'currency', currency: cur }).format(n);
  return (
    <section>
      <h2>Payment History</h2>
      <table>
        <thead><tr><th>Date</th><th>Amount</th><th>Method</th><th>Status</th></tr></thead>
        <tbody>
          {payments.map(p => (
            <tr key={p.paymentId}>
              <td>{new Date(p.date).toLocaleDateString()}</td>
              <td>{fmt(p.amount, 'USD')}</td>
              <td>{p.method}</td>
              <td>{p.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
