import React from 'react';
import { usePremiumUpdates } from '../hooks/usePremiumUpdates';
import { IPremium } from '../types';

type Props = { policyId: string };
export const PremiumStatus: React.FC<Props> = ({ policyId }) => {
  const { premium } = usePremiumUpdates(policyId);
  if (!premium) return <div>Loading premium...</div>;
  const formatted = new Intl.NumberFormat(undefined, { style: 'currency', currency: premium.currency }).format(premium.currentAmount);
  return (
    <section>
      <h2>Premium Status</h2>
      <p>Current Amount: {formatted}</p>
      <p>Next Due: {premium.nextDueDate ? new Date(premium.nextDueDate).toLocaleDateString() : 'N/A'}</p>
      <p>Status: {premium.status}</p>
    </section>
  );
}
