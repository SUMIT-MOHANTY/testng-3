import React from 'react';
import { RoleGuard } from '../router/RoleGuard';
import { PolicyOverview } from '../components/PolicyOverview';
import { PremiumStatus } from '../components/PremiumStatus';
import { PaymentHistory } from '../components/PaymentHistory';
import { ClaimSubmission } from '../components/ClaimSubmission';
import { useAuth } from '../hooks/useAuth';
import styles from './Dashboard.module.scss';

export const Dashboard: React.FC = () => {
  const { user } = useAuth();
  const policyId = user?.policyId || '';
  return (
    <RoleGuard allowedRoles={['policy_holder', 'admin']}>
      <div className={styles.grid}>
        <PolicyOverview policyId={policyId} />
        <PremiumStatus policyId={policyId} />
        <PaymentHistory policyId={policyId} />
        <ClaimSubmission policyId={policyId} />
      </div>
    </RoleGuard>
  );
}
