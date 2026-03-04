import React from 'react';
import { useForm } from 'react-hook-form';
import { IClaimForm } from '../types';
import { submitClaim } from '../services/claim_service';
import { FileUploader } from '../FileUploader';
import styles from './claim-submission.module.scss';

type Props = { policyId: string };
export const ClaimSubmission: React.FC<Props> = ({ policyId }) => {
  const { register, handleSubmit, formState: { errors }, setValue } = useForm<IClaimForm>();
  const onSubmit = async (data: IClaimForm) => {
    const formData = new FormData();
    formData.append('policyId', data.policyId);
    formData.append('claimType', data.claimType);
    formData.append('description', data.description);
    if (data.attachment) formData.append('attachment', data.attachment);
    await submitClaim(formData);
    alert('Claim submitted');
  };
  const handleFile = (file: File) => setValue('attachment', file);
  return (
    <section className={styles.container}>
      <h2>Submit Claim</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input type="hidden" {...register('policyId')} value={policyId} />
        <div>
          <label>Claim Type</label>
          <input {...register('claimType', { required: true })} />
          {errors.claimType && <span>Required</span>}
        </div>
        <div>
          <label>Description</label>
          <textarea {...register('description', { required: true })} />
          {errors.description && <span>Required</span>}
        </div>
        <div>
          <label>Attachment</label>
          <FileUploader onFileSelect={handleFile} accept=".pdf,.jpg,.png" />
          {errors.attachment && <span>Required</span>}
        </div>
        <button type="submit">Submit</button>
      </form>
    </section>
  );
}
