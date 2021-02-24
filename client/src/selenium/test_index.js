require("dotenv").config();

const { Builder, By, Key, until } = require("selenium-webdriver");
(async function example() {
  let driver = await new Builder().forBrowser("chrome").build();

  await driver.get(process.env.VUE_APP_BASE_URL);
  await driver
    .findElement(By.name("input_search"))
    .sendKeys("erevan", Key.RETURN)
    .then(function() {
        setTimeout(function() {
            driver
            .findElement(By.name("input_search"))
            .sendKeys("musée d'orsay", Key.RETURN);
        }, 5000)
    })
})();
