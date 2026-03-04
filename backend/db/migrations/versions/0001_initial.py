from alembic import op
import sqlalchemy as sa

def upgrade():
    # users table
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("email", sa.String(255), unique=True, nullable=False),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("role", sa.String(50), nullable=False),
    )
    # accounts table
    op.create_table(
        "accounts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("type", sa.String(50), nullable=False),
        sa.Column("balance", sa.Numeric(12, 2), nullable=False, server_default="0"),
    )
    # insurance_policies table
    op.create_table(
        "insurance_policies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("policy_number", sa.String(50), unique=True, nullable=False),
        sa.Column("coverage_amount", sa.Numeric(12, 2), nullable=False),
        sa.Column("premium", sa.Numeric(12, 2), nullable=False),
        sa.Column("effective_date", sa.Date, nullable=False),
        sa.Column("expiry_date", sa.Date, nullable=False),
    )
    # transactions table
    op.create_table(
        "transactions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("account_id", sa.Integer, sa.ForeignKey("accounts.id"), nullable=False),
        sa.Column("amount", sa.Numeric(12, 2), nullable=False),
        sa.Column("timestamp", sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column("description", sa.String(255)),
    )
    # loans table
    op.create_table(
        "loans",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("principal", sa.Numeric(12, 2), nullable=False),
        sa.Column("interest_rate", sa.Numeric(5, 4), nullable=False),
        sa.Column("term_months", sa.Integer, nullable=False),
        sa.Column("status", sa.String(20), nullable=False, server_default="pending"),
    )
    # claims table
    op.create_table(
        "claims",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("policy_id", sa.Integer, sa.ForeignKey("insurance_policies.id"), nullable=False),
        sa.Column("claim_number", sa.String(50), unique=True, nullable=False),
        sa.Column("amount_requested", sa.Numeric(12, 2), nullable=False),
        sa.Column("status", sa.String(20), nullable=False, server_default="submitted"),
        sa.Column("filed_at", sa.DateTime, server_default=sa.func.now(), nullable=False),
    )

def downgrade():
    op.drop_table("claims")
    op.drop_table("loans")
    op.drop_table("transactions")
    op.drop_table("insurance_policies")
    op.drop_table("accounts")
    op.drop_table("users")
