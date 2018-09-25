package org.python.test;
import static org.junit.Assert.assertEquals;
import org.python.exceptions.IndexError;
import org.python.types.List;
import org.python.types.Int;
import org.python.types.Object;
import org.python.types.Bool;
import org.python.types.Str;
import java.util.*;
import org.junit.Test;
import junit.framework.TestCase;

public class JavaTest extends TestCase {

    // ----------------- Erika and Daniel------------------

    @Test
    public void testCreation() {
        List x = new List();
        assertTrue(x.__len__() == Int.getInt(0));
    }

    @Test
    public void testAppend() {
        List x = new List();

        // Appending items
        Object firstInt = Int.getInt(7);
        Object secondInt = Int.getInt(2);
        x.append(firstInt);
        x.append(secondInt);
        Bool firstIntExist = (Bool) x.__contains__(firstInt);
        assertTrue(firstIntExist.value);

        // Testappending mixed types in list
        Str s = new Str("hello");
        x.append(s);
        Bool strInList = (Bool) x.__contains__(s);
        assertTrue(strInList.value && firstIntExist.value);
    }

    @Test
    public void testGetitem() {
        List x = new List();
        Object obj1 = new Str("some string");
        Object obj2 = new Str("another string");
        Object obj3 = new Str("again and again");
        Object obj4 = new Str("random stuff");

        x.append(obj1);
        x.append(obj2);
        x.append(obj3);
        x.append(obj4);

        assertEquals(((Str)x.__getitem__(Int.getInt(2))).value, "again and again");
    }

    @Test
    public void testSetitem() {
        // set object in list where another object exists
        List x1 = new List();
        x1.append(Int.getInt(1));
        x1.__setitem__(Int.getInt(0), Int.getInt(5));
        assertEquals(x1.__getitem__(Int.getInt(0)), Int.getInt(5));


    }

    @Test
    public void testSetitemDifferentTypes() {
        // set object in list where another object exists with different type.
        List x2 = new List();

        x2.append(Int.getInt(1));
        x2.append(Int.getInt(2));
        x2.append(Int.getInt(3));

        x2.__setitem__(Int.getInt(1), new Str("hello"));
        x2.__setitem__(Int.getInt(2), new Str("there"));
        assertTrue(x2.__getitem__(Int.getInt(0)) == Int.getInt(1) && 
                            ((Str)x2.__getitem__(Int.getInt(1))).value == "hello" &&
                            ((Str)x2.__getitem__(Int.getInt(2))).value == "there");
    }

    @Test(expected = IndexError.class)
    public void testSetItemOutOfBounds() {
        List x = new List();
        try {
            x.__setitem__(Int.getInt(0), Int.getInt(5));
        } catch(IndexError e) {}

    }

    @Test(expected = IndexError.class)
    public void testSetItemOutOfBoundsNegative() {
        // try to set item on negative index
        List x = new List();
        x.append(Int.getInt(1));
        try {
            x.__setitem__(Int.getInt(-2), Int.getInt(5));
        } catch(IndexError e) {}

    }

    // -------------------------------------------------------
    
    
    
    // --------- Adam, Tor and Jakob ---------------------------
    // -----------------------------------------------------------

    // --------- Lucas and Henrik -------------------------------
    // ----------------------------------------------------------
    
}
