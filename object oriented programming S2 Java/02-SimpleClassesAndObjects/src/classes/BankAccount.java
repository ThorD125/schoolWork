package classes;

import java.util.Objects;

public class BankAccount {

    private Person owner;
    private double balance;
    private String accountNumber;

    public String tostrString() {
        return "Owner: " + owner.getName() + " has a balance of: " + balance;
    }

    public BankAccount(Person eowner) {
        owner = eowner;
        balance = 0;
        accountNumber = "generic";
    }

    public BankAccount(Person eowner, String eaccountNumber) {
        owner = eowner;
        balance = 0;
        accountNumber = eaccountNumber;
    }

    public boolean equals(BankAccount other) {

        return accountNumber.equals(other.accountNumber);
    }

    public String withdraw(double amount) {
        if (amount > balance) {
            return "Insufficient withdraw funds";
        } else if (amount <= 0) {
            return "Invalid withdraw amount";
        } else {
            balance = Math.round(balance - amount);
            return "Withdraw was succesfull";
        }
    }
    @Override
    public int hashCode() {
        return Objects.hash(accountNumber);
    }

    public String deposit(double amount) {
        if (amount <= 0) {
            return "Invalid deposit amount";
        } else {
            balance = Math.round(balance + amount);
            return "Deposit was succesfull";
        }
    }

    public String transfer(BankAccount target, double amount) {

        if ((this.withdraw(amount) == "Withdraw was succesfull")
                && ("Withdraw was succesfull" == target.deposit(amount))) {
            this.withdraw(amount);
            target.deposit(amount);
            return "Transaction was succesfull";
        } else {
            return "Transaction was invalid";
        }

    }

}
