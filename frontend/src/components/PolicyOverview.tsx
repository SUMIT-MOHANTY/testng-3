import React, { useEffect, useState } from 'react';
import { IPolicy } from '../types';
import { getPolicy } from '../services/policy_service';

type Props = { policyId: string };
export const PolicyOverview: React.FC<Props> = ({ policyId }) => {
  const [policy, setPolicy] = useState<IPolicy | null>(null);
  useEffect(() => { getPolicy(policyId).then(setPolicy); }, [policyId]);
  if (!policy) return <div>Loading policy...</div>;
  return (
    <section>
      <h2>Policy Overview</h2>
      <p><strong>Number:</strong> {policy.policyNumber}</p>
      <p><strong>Holder:</strong> {policy.holderName}</p>
      <p><strong>Effective:</strong> {new Date(policy.effectiveDate).toLocaleDateString()}</p>
      <p><strong>Expiry:</strong> {new Date(policy.expiryDate).toLocaleDateString()}</p>
      <p><strong>Coverage:</strong> {policy.coverageType}</p>
    </section>
  );
}
