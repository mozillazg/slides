package com.mycompany.app;

import java.util.logging.Level;
import java.util.logging.Logger;

class MyClass {
    private static final Logger logger = Logger.getLogger(MyClass.class.getName());

    void logSimpleMessage() {
        // This adds a simple message to the logs
        logger.log(Level.INFO, "This is a test");
    }

    void logException() {
        try {
            unsafeMethod();
        } catch (Exception e) {
            // This adds an exception to the logs
            logger.log(Level.SEVERE, "Exception caught", e);
        }
    }

    void unsafeMethod() {
        throw new UnsupportedOperationException("You shouldn't call that");
    }
}

public class App {
    public static void main( String[] args ) {
        MyClass cls = new MyClass();
        cls.logException();
        System.out.println( "Hello World!" );
    }
}
