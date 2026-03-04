export interface IPolicy {
  policyNumber: string;
  holderName: string;
  effectiveDate: string;
  expiryDate: string;
  coverageType: string;
}

export interface IPremium {
  currentAmount: number;
  nextDueDate?: string;
  currency: string;
  status?: 'charged' | 'pending';
}

export interface IPayment {
  paymentId: string;
  date: string;
  amount: number;
  method: string;
  status: string;
}

export interface IClaimForm {
  policyId: string;
  claimType: string;
  description: string;
  attachment: File | null;
}
