# Auto-gform
Get shudh indian responses on your Gform :) 

## steps to initialize
- Clone this repository and open terminal in the root of this repository. Install and create a virtual environment
<pre>pip install virtualenv</pre>
<pre>virtualenv auto</pre>

- You would need a chrome driver for this. I have provided chromedriver for chrome version 10.1, you can get chromedriver according to your machine <a href="https://chromedriver.chromium.org/downloads">here</a>. After downloading, place this chromedriver in this filder's root.

- After acting virtual environment created earlier, run the below code in the root of this repository.
After the virtual environment is activated, it will be shown in following way
### (auto) path\to\your\folder

> note, each g-form is different and contain various combinations of different input fields. So modify the script accordingly. 
<pre>job.sh</pre>

It will install the required dependencies and open another terminal window. There provide the number of responses you want to inject and BOOM!
the script works.

## Usage
- Enter your google form URL
- Select number of responses.

## Upcoming
> recaptcha bypass <br>
> More user friendly flow
