import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.Assert;

public class MainClassTest {

    @Test
    public void testGetLocalNumber() {
        Assert.assertTrue("Значение метода getLocalNumber не соответствует заявленному" , MainClass.getLocalNumber() == 14);

    }

}
