import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.net.URL;

public class FirstTest {

    private AppiumDriver driver;

    @Before
    public void setUp() throws Exception {
        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("platformName", "Android");
        capabilities.setCapability("deviceName", "AndroidTestDevice");
        capabilities.setCapability("platformVersion", "6.0");
        capabilities.setCapability("AutomationName", "Appium");
        capabilities.setCapability("appPackage", "org.wikipedia");
        capabilities.setCapability("appActivity", ".main.MainActivity");
        capabilities.setCapability("app", "C:\\Users\\gkazarkin\\Downloads\\Auto\\Уроки\\AppiumTests\\apks\\org.wikipedia.apk");

        driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);
    }

    @After
    public void tearDown() {
        driver.quit();
    }

    @Test
    public void firstTest() {

        //Создаём элемент и вызываем аппиум, найти по Xpath, искать в любой вложенности, любой элемент
        //contains позволяет искать по частичному совпадению текста

        WebElement element_to_init_search = driver.findElementByXPath("//*[contains(@text, 'Search Wikipedia')]");
        element_to_init_search.click();

       WebElement element_to_enter_search_line = waitForElementPresentByXpath("//*[contains(@text, 'Search…')]",
"Cannot find Search input", 5);
        
    }

    //Ожидание появление элемента по Xpath
    private WebElement waitForElementPresentByXpath(String xpath, String error_message, long timeoutInSeconds) {
        WebDriverWait wait = new WebDriverWait(driver, timeoutInSeconds);
        //Сообщение об ошибке
        wait.withMessage(error_message + "\n");
        //Передаём параметр по которому ожидаем
        By by = By.xpath(xpath);
        //Возвращаем то, что ждём пока не будет искомый Xpath
        return wait.until(ExpectedConditions.presenceOfElementLocated(by));
    }

}