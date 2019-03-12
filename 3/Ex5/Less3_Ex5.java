import io.appium.java_client.AppiumDriver;
import io.appium.java_client.TouchAction;
import io.appium.java_client.android.AndroidDriver;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.ScreenOrientation;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.net.URL;
import java.util.List;

public class Less3_Ex5 {

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
    public void saveArticlesToMyListAndDeleteOne() {
        waitForElementAndClick(By.xpath("//*[contains(@text, 'Search Wikipedia')]"), "Cannot find 'Search Wikipedia'",
                5 );

        waitForElementAndSendKeys(By.xpath("//*[contains(@text, 'Search…')]"), "Java", "Cannot input text 'Java'",
                5);

        waitForElementAndClick(
                By.xpath("//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='Object-oriented programming language']"),
                "Cannot find text after searching", 5);

        waitForElementPresent(By.id("org.wikipedia:id/view_page_title_text"),
                "Cannot find article title about 'Java' ",
                10);

        waitForElementAndClick(
                By.xpath("//android.widget.ImageView[@content-desk='More options']"),
                "Cannot find button to open article options", 5);

        waitForElementAndClick(By.xpath("//*[@text='Add to reading list']"),
                "Cannot find option to add article to reading list", 5);

        waitForElementAndClick(By.id("org.wikipedia:id/onboarding_button"),
                "Cannot find button 'GOT IT' tip overlay", 5);

        waitForElementAndClear(By.id("org.wikipedia:id/text_input"),
                "Cannot find input to set name of article folder", 5);

        String name_of_folder = "Learning programming";
        waitForElementAndSendKeys(By.id("org.wikipedia:id/text_input"),
                name_of_folder, "Cannot put text into articles folder input", 5);

        waitForElementAndClick(By.xpath("//*[@content-desk='OK'"),
                "Cannot press 'OK' button", 5);

        waitForElementAndClick(By.xpath("//android.widget.ImageButton[@content-desk='Navigate up'"),
                "Cannot close article or cannot find 'X' button", 5);

        //Добавление 2ой статьи
        waitForElementAndClick(By.xpath("//*[contains(@text, 'Search Wikipedia')]"), "Cannot find 'Search Wikipedia'",
                5 );

        waitForElementAndSendKeys(By.xpath("//*[contains(@text, 'Search…')]"), "Appius", "Cannot input text 'Appius'",
                5);

        waitForElementAndClick(
                By.xpath("//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='Roman politician']"),
                "Cannot find text after searching", 5);

        waitForElementPresent(By.id("org.wikipedia:id/view_page_title_text"),
                "Cannot find article title about 'Appius Claudius Caecus' ",
                10);

        waitForElementAndClick(
                By.xpath("//android.widget.ImageView[@content-desk='More options']"),
                "Cannot find button to open article options", 5);

        waitForElementAndClick(By.xpath("//*[@text='Add to reading list']"),
                "Cannot find option to add article to reading list", 5);

        waitForElementAndClick(By.id("org.wikipedia:id/create_button"),
                "Cannot find button 'Create new' tip overlay", 5);

        waitForElementAndClear(By.id("org.wikipedia:id/text_input"),
                "Cannot find input to set name of article folder", 5);

        String name_of_folder2 = "Appius Claudius Caecus";
        waitForElementAndSendKeys(By.id("org.wikipedia:id/text_input"),
                name_of_folder2, "Cannot put text into articles folder input", 5);

        waitForElementAndClick(By.xpath("//*[@content-desk='OK'"),
                "Cannot press 'OK' button", 5);

        waitForElementAndClick(By.xpath("//android.widget.ImageButton[@content-desk='Navigate up'"),
                "Cannot close article or cannot find 'X' button", 5);

        //Переход в избранное
        waitForElementAndClick(By.xpath("//android.widget.FrameLayout[@content-desk='My lists'"),
                "Cannot find navigation button to 'My lists'", 5);

        waitForElementAndClick(By.xpath("//android.widget.FrameLayout[@content-desk='My lists'"),
                "Cannot find navigation button to 'My lists'", 5);

        waitForElementAndClick(By.xpath("//*[@text='" + name_of_folder + "']"),
                "Cannot find created folder in 'My lists'", 5);

        swipeElementToLeft(By.xpath("//*[@text='Java (programming language)']"),
                "Cannot find saved article about 'Java'");

        waitForElementAndClick(By.xpath("//*[@text='Appius']"), "Saved article about 'Appius Claudius Caecus' isn't present",
                15 );

        WebElement title_element = waitForElementPresent(
                By.id("org.wikipedia:id/view_page_title_text"), "Cannot find text about 'Appius' to check title article",
                15);
        String article_title = title_element.getAttribute("text");
        Assert.assertEquals("Unexpected title not about 'Appius'", article_title, "Appius Claudius Caecus" );
    }

    private WebElement waitForElementPresent(By by, String error_message, long timeoutInSeconds) {
        WebDriverWait wait = new WebDriverWait(driver, timeoutInSeconds);
        wait.withMessage(error_message);
        return wait.until(ExpectedConditions.presenceOfElementLocated(by));
    }

    private WebElement waitForElementPresent(By by, String error_message) {
        return waitForElementPresent(by, error_message, 5);
    }

    private WebElement waitForElementAndClick(By by, String error_message, long timeoutInSeconds) {
        WebElement element = waitForElementPresent(by, error_message, timeoutInSeconds);
        element.click();
        return element;
    }

    private WebElement waitForElementAndSendKeys(By by, String value, String error_message, long timeoutInSeconds) {
        WebElement element = waitForElementPresent(by, error_message, timeoutInSeconds);
        element.sendKeys(value);
        return element;
    }


    private boolean waitForElementNotPresent(By by, String error_message, long timeoutInSeconds) {
        WebDriverWait wait = new WebDriverWait(driver, timeoutInSeconds);
        wait.withMessage(error_message + "\n");
        return wait.until(ExpectedConditions.invisibilityOfElementLocated(by));
    }

    private WebElement waitForElementAndClear(By by, String error_message, long timeoutInSeconds) {
        WebElement element = waitForElementPresent(by, error_message, timeoutInSeconds);
        element.clear();
        return element;
    }

    protected void swipeUp(int timeOfSwipe) {
        TouchAction action = new TouchAction(driver);
        Dimension size = driver.manage().window().getSize();
        int x = size.width / 2;
        int start_y = (int) (size.height * 0.8);
        int end_y = (int) (size.height * 0.2);

        action
                .press(x, start_y)
                .waitAction(timeOfSwipe)
                .moveTo(x, end_y)
                .release()
                .perform();
    }

    protected void swipeUpQuick() {
        swipeUp(200);
    }

    protected void swipeUpToFindElement(By by,String error_message, int max_swipes) {

        driver.findElements(by).size();

        int already_swiped = 0;
        while (driver.findElements(by).size() == 0) {
            if (already_swiped > max_swipes) {
                waitForElementPresent(by, "Cannot find element by swiping up \n" + error_message, 0);
                return;
            }
            swipeUpQuick();
            ++already_swiped;
        }
    }

    protected void swipeElementToLeft(By by, String error_message) {

        WebElement element = waitForElementPresent(by, error_message, 10);
        int left_x = element.getLocation().getX();
        int right_x = left_x + element.getSize().getWidth();
        int upper_y = element.getLocation().getY();
        int lower_y = upper_y + element.getSize().getHeight();
        int middle_y = (upper_y + lower_y) / 2;

        TouchAction action = new TouchAction(driver);
        action
                .press(right_x, middle_y)
                .waitAction(300)
                .moveTo(left_x, middle_y)
                .release()
                .perform();
    }

}