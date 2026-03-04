import { useEffect, useState } from 'react';
import { IPremium } from '../types';
import { subscribePremiumUpdates } from '../services/premium_service';

export const usePremiumUpdates = (policyId: string) => {
  const [premium, setPremium] = useState<IPremium | null>(null);
  const [error, setError] = useState<Error | null>(null);
  useEffect(() => {
    const host = process.env.REACT_APP_API_HOST || '';
    const url = `wss://${host}/ws/premium-updates?policyId=${policyId}`;
    const unsubscribe = subscribePremiumUpdates(url, setPremium);
    return () => unsubscribe();
  }, [policyId]);
  return { premium, error };
};
