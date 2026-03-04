describe('Auth Flow', () => {
  it('registers, logs in, and logs out', () => {
    cy.visit('/register');
    cy.get('input[name="email"]').type('test@example.com');
    cy.get('input[name="password"]').type('Password123');
    cy.get('input[name="confirmPassword"]').type('Password123');
    cy.contains('Register').click();
    cy.url().should('include', '/dashboard');
    cy.contains('Logout').click();
    cy.url().should('include', '/login');
  });
});
