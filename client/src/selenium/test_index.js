require("dotenv").config();

const { Builder, By, Key, until } = require("selenium-webdriver");
(async function example() {
  let driver = await new Builder().forBrowser("chrome").build();

  await driver.get(process.env.VUE_APP_BASE_URL);
  await driver
    .findElement(By.name("input_search"))
    .then(function() {
        setTimeout(function() {
            driver
            .findElement(By.name("input_search"))
            .sendKeys("erevan", Key.RETURN)
            driver.wait(until.elementLocated(By.id('wiki_text')), 1000);
            driver.wait(until.elementLocated(By.id('temp_slnm')), 1000);
            driver.wait(until.elementLocated(By.id('icon_weather')), 1000);
            driver.wait(until.elementLocated(By.id('message_slnm')), 1000);
            driver.wait(until.elementLocated(By.id('map_widget')), 1000);
        }, 5000)
    })
})();
