import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.Assert;

public class MainClassTest {

    @Test
    public void testGetLocalNumber() {
        Assert.assertTrue("Значение метода getLocalNumber не равно 14", MainClass.getLocalNumber() == 14);

    }

    @Test
    public void testGetClassNumber() {
        Assert.assertTrue("Значение метода GetClassNumber меньше или равно 45",MainClass.getClassNumber() > 45);
    }

    @Test
    public void testGetClassString() {
        Assert.assertTrue("Значение метода getClassString не содержит строк hello или Hello",MainClass.getClassString().contains("hello") || MainClass.getClassString().contains("Hello"));
    }
}
