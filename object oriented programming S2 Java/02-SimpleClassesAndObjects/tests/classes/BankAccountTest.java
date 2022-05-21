package classes;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class BankAccountTest {

    @Test
    void tostrString() {
        Person me = new Person("Mattias", 123);
        BankAccount myAccount = new BankAccount(me);
        assertEquals("Owner: Mattias has a balance of: 0.0", myAccount.tostrString());

        myAccount.deposit(15.098);

        assertEquals("Owner: Mattias has a balance of: 15.0", myAccount.tostrString());

    }

    @Test
    void deposit() {
        Person me = new Person("Mattias", 123);
        BankAccount myAccount = new BankAccount(me);

        assertEquals("Invalid deposit amount", myAccount.deposit(0));
        assertEquals("Invalid deposit amount", myAccount.deposit(-10));
        assertEquals("Deposit was succesfull", myAccount.deposit(100));

    }

    @Test
    void withdraw() {

        Person me = new Person("Mattias", 123);
        BankAccount myAccount = new BankAccount(me);
        myAccount.deposit(100);

        assertEquals("Invalid withdraw amount", myAccount.withdraw(0));
        assertEquals("Invalid withdraw amount", myAccount.withdraw(-10));
        assertEquals("Withdraw was succesfull", myAccount.withdraw(100));

    }

    @Test
    void equals() {
        Person me = new Person("Mattias", 123);
        BankAccount myAccount = new BankAccount(me, "selkfjseml");
        BankAccount myAccount2 = new BankAccount(me, "selkfjseml");

        Person me3 = new Person("jeffrey", 123);
        BankAccount myAccount3 = new BankAccount(me, "selkfjsemlesefsfes");

        assertEquals(true, myAccount.equals(myAccount2));
        assertEquals(false, myAccount.equals(myAccount3));
    }

    @Test
    void transfer() {
        Person me = new Person("Mattias", 123);
        BankAccount myAccount = new BankAccount(me);

        Person me2 = new Person("Mattias", 123);
        BankAccount myAccount2 = new BankAccount(me2);

        myAccount.deposit(150);

        myAccount.transfer(myAccount2, 15);
        assertEquals("Owner: Mattias has a balance of: 135.0", myAccount.tostrString());

        // assertEquals("Transaction was succesfull", myAccount.transfer(myAccount2,
        // 15));
        // assertEquals("Transaction was invalid", myAccount.transfer(myAccount2, 15));
    }
}