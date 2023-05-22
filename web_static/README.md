<h1>0x01. AirBnB clone - Web static</h1>
<div>
    <div>HTMLCSSFront-end</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Guillaume</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">May 18, 2023 6:00 AM</span>, must end by&nbsp;<span title="">May 23, 2023 6:00 AM</span></li>
        <li>&nbsp;<strong>Manual QA review must be done</strong> (request it when you are done with the project)</li>
    </ul>
</div>
<div>
    <div>
        <h3>Concepts</h3>
    </div>
    <div>
        <p><em>For this project, we expect you to look at these concepts:</em></p>
        <ul>
            <li><a href="https://intranet.alxswe.com/concepts/2">HTML/CSS</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/4">The trinity of front-end quality</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/9/135ef103cf7ed150c9760aadc66844113dfc3d35.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1507877dd9786bdd318960233ba78bb4649f082bfa8a008476919b047cd387d2" alt=""></p>
        <h2>Background Context</h2>
        <h3>Web static, what?</h3>
        <p>Now that you have a command interpreter for managing your AirBnB objects, it&rsquo;s time to make them alive!</p>
        <p>Before developing a big and complex web application, we will build the front end step-by-step.</p>
        <p>The first step is to &ldquo;design&rdquo; / &ldquo;sketch&rdquo; / &ldquo;prototype&rdquo; each element:</p>
        <ul>
            <li>Create simple HTML static pages</li>
            <li>Style guide</li>
            <li>Fake contents</li>
            <li>No Javascript</li>
            <li>No data loaded from anything</li>
        </ul>
        <p>During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can&rsquo;t apply any design.</p>
        <p>Before starting, please fork or clone the repository&nbsp;<code>AirBnB_clone</code> from your partner if you were not the owner of the previous project.</p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/T9KyiA6_Tm3Ny6oTn08S-A" title="Learn to Code HTML & CSS" target="_blank">Learn to Code HTML &amp; CSS</a> (<em>until &ldquo;Creating Lists&rdquo; included</em>)</li>
            <li><a href="https://intranet.alxswe.com/rltoken/7NdYbImFNofpB_FXXn3otg" title="Inline Styles in HTML" target="_blank">Inline Styles in HTML</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/z_OTPFCjmhXJJi7KJqBCbQ" title="Specifics on CSS Specificity" target="_blank">Specifics on CSS Specificity</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/orI812cozq-yd2769VdM_w" title="CSS SpeciFishity" target="_blank">CSS SpeciFishity</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/okP4V3RxFXHkEcQo19AnuQ" title="Introduction to HTML" target="_blank">Introduction to HTML</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/Ir8Ka59FO6Z_vJQ-gkSG_w" title="CSS" target="_blank">CSS</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/BpSXtcWOGH0UT4XLCoQyJg" title="MDN" target="_blank">MDN</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/Tlje4XYwyZbUfHkQWGi1WQ" title="center boxes" target="_blank">center boxes</a></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/Zb9sTIct2xdhDCDLGF-RyQ" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>What is HTML</li>
            <li>How to create an HTML page</li>
            <li>What is a markup language</li>
            <li>What is the DOM</li>
            <li>What is an element / tag</li>
            <li>What is an attribute</li>
            <li>How does the browser load a webpage</li>
            <li>What is CSS</li>
            <li>How to add style to an element</li>
            <li>What is a class</li>
            <li>What is a selector</li>
            <li>How to compute CSS Specificity Value</li>
            <li>What are Box properties in CSS</li>
        </ul>
        <h3>Copyright - Plagiarism</h3>
        <ul>
            <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
            <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</li>
            <li>You are not allowed to publish any content of this project.</li>
            <li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
        </ul>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files should end with a new line</li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should be W3C compliant and validate with&nbsp;<a href="https://intranet.alxswe.com/rltoken/NzQ96QXtBTCMRDicPORzbA" title="W3C-Validator" target="_blank">W3C-Validator</a></li>
            <li>All your CSS files should be in&nbsp;<code>styles</code> folder</li>
            <li>All your images should be in&nbsp;<code>images</code> folder</li>
            <li>You are not allowed to use&nbsp;<code>!important</code> and&nbsp;<code>id</code> (<code>#...</code> in the CSS file)</li>
            <li>You are not allowed to use tags&nbsp;<code>img</code>,&nbsp;<code>embed</code> and&nbsp;<code>iframe</code></li>
            <li>You are not allowed to use Javascript</li>
            <li>Current screenshots have been done on&nbsp;<code>Chrome 56</code> or more.</li>
            <li>No cross browsers</li>
            <li>You have to follow all requirements but some&nbsp;<code>margin</code>/<code>padding</code> are missing - you should try to fit as much as you can to screenshots</li>
        </ul>
        <h2>More Info</h2>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png" alt=""></p>
    </div>
</div>
<div>
    <div>
        <h3>Quiz questions</h3>
    </div>
    <div>
        <div><strong>Great!</strong> You&apos;ve completed the quiz successfully! Keep going!&nbsp;(Show quiz)</div>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. Inline styling</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header and a footer.</p>
            <p>Layout:</p>
            <ul>
                <li>Body:<ul>
                        <li>no margin</li>
                        <li>no padding</li>
                    </ul>
                </li>
                <li>Header:<ul>
                        <li>color #FF0000 (red)</li>
                        <li>height: 70px</li>
                        <li>width: 100%</li>
                    </ul>
                </li>
                <li>Footer:<ul>
                        <li>color #00FF00 (green)</li>
                        <li>height: 60px</li>
                        <li>width: 100%</li>
                        <li>text&nbsp;<code>Best School</code> center vertically and horizontally</li>
                        <li>always at the bottom at the page</li>
                    </ul>
                </li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>header</code> and&nbsp;<code>footer</code> tags</li>
                <li>You are not allowed to import any files</li>
                <li>You are not allowed to use the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag</li>
                <li>Use inline styling for all your tags</li>
            </ul>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/98f4ac1b0644512ce7ae91a9e8e61e8fe174911d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0419eb955fe0fce381626f380043c77ef2b5c4e057f1d9659547c4d1646af2cb" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>0-index.html</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. Head styling</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header and a footer by using the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag (same as&nbsp;<code>0-index.html</code>)</p>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>header</code> and&nbsp;<code>footer</code> tags</li>
                <li>You are not allowed to import any files</li>
                <li>No inline styling</li>
                <li>You must use the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag</li>
            </ul>
            <p>The layout must be exactly the same as&nbsp;<code>0-index.html</code></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>1-index.html</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. CSS files</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header and a footer by using CSS files (same as&nbsp;<code>1-index.html</code>)</p>
            <p>Requirements:</p>
            <ul>
                <li>You must use the&nbsp;<code>header</code> and&nbsp;<code>footer</code> tags</li>
                <li>No inline styling</li>
                <li>You must have 3 CSS files:<ul>
                        <li><code>styles/2-common.css</code>: for global style (i.e. the&nbsp;<code>body</code> style)</li>
                        <li><code>styles/2-header.css</code>: for header style</li>
                        <li><code>styles/2-footer.css</code>: for footer style</li>
                    </ul>
                </li>
            </ul>
            <p>The layout must be exactly the same as&nbsp;<code>1-index.html</code></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>3. Zoning done!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header and footer by using CSS files (same as&nbsp;<code>2-index.html</code>)</p>
            <p>Layout:</p>
            <ul>
                <li>Common:<ul>
                        <li>no margin</li>
                        <li>no padding</li>
                        <li>font color: #484848</li>
                        <li>font size: 14px</li>
                        <li>font family:&nbsp;<code>Circular,&quot;Helvetica Neue&quot;,Helvetica,Arial,sans-serif;</code></li>
                        <li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png" title="icon" target="_blank">icon</a> in the browser tab</li>
                    </ul>
                </li>
                <li>Header:<ul>
                        <li>color: white</li>
                        <li>height: 70px</li>
                        <li>width: 100%</li>
                        <li>border bottom 1px #CCCCCC</li>
                        <li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png" title="logo" target="_blank">logo</a> align on left and center vertically (20px space at the left)</li>
                    </ul>
                </li>
                <li>Footer:<ul>
                        <li>color white</li>
                        <li>height: 60px</li>
                        <li>width: 100%</li>
                        <li>border top 1px #CCCCCC</li>
                        <li>text&nbsp;<code>Best School</code> center vertically and horizontally</li>
                        <li>always at the bottom at the page</li>
                    </ul>
                </li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>No inline style</li>
                <li>You are not allowed to use the&nbsp;<code>img</code> tag</li>
                <li>You are not allowed to use the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag</li>
                <li>All images must be stored in the&nbsp;<code>images</code> folder</li>
                <li>You must have 3 CSS files:<ul>
                        <li><code>styles/3-common.css</code>: for the global style (i.e&nbsp;<code>body</code> style)</li>
                        <li><code>styles/3-header.css</code>: for the header style</li>
                        <li><code>styles/3-footer.css</code>: for the footer style</li>
                    </ul>
                </li>
            </ul>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/2be1eda05a0d9097c210f2d3482a59aa858c5711.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e810dc7015945ac2e2275c98ec1d7b9512d8f93adddd4c4df4baf18fe3fc4c95" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>4. Search!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header, footer and a filters box with a search button.</p>
            <p>Layout: (based on&nbsp;<code>3-index.html</code>)</p>
            <ul>
                <li>Container:<ul>
                        <li>between&nbsp;<code>header</code> and&nbsp;<code>footer</code> tags, add a&nbsp;<code>div</code>:<ul>
                                <li>classname:&nbsp;<code>container</code></li>
                                <li>max width 1000px</li>
                                <li>margin top and bottom 30px - it should be 30px under the bottom of the&nbsp;<code>header</code> (screenshot)</li>
                                <li>center horizontally</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>Filter section:<ul>
                        <li>tag&nbsp;<code>section</code></li>
                        <li>classname&nbsp;<code>filters</code></li>
                        <li>inside the&nbsp;<code>.container</code></li>
                        <li>color white</li>
                        <li>height: 70px</li>
                        <li>width: 100% of the container</li>
                        <li>border 1px #DDDDDD with radius 4px</li>
                    </ul>
                </li>
                <li>Button search:<ul>
                        <li>tag&nbsp;<code>button</code></li>
                        <li>text&nbsp;<code>Search</code></li>
                        <li>font size: 18px</li>
                        <li>inside the section filters</li>
                        <li>background color #FF5A5F</li>
                        <li>text color #FFFFFF</li>
                        <li>height: 48px</li>
                        <li>width: 20% of the section filters</li>
                        <li>no borders</li>
                        <li>border radius: 4px</li>
                        <li>center vertically and at 30px of the right border</li>
                        <li>change opacity to 90% when the mouse is on the button</li>
                    </ul>
                </li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use:&nbsp;<code>header</code>,&nbsp;<code>footer</code>,&nbsp;<code>section</code>,&nbsp;<code>button</code> tags</li>
                <li>No inline style</li>
                <li>You are not allowed to use the&nbsp;<code>img</code> tag</li>
                <li>You are not allowed to use the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag</li>
                <li>All images must be stored in the&nbsp;<code>images</code> folder</li>
                <li>You must have 4 CSS files:<ul>
                        <li><code>styles/4-common.css</code>: for the global style (<code>body</code> and&nbsp;<code>.container</code> styles)</li>
                        <li><code>styles/3-header.css</code>: for the header style</li>
                        <li><code>styles/3-footer.css</code>: for the footer style</li>
                        <li><code>styles/4-filters.css</code>: for the filters style</li>
                    </ul>
                </li>
                <li><code>4-index.html</code> <strong>won&rsquo;t be W3C valid</strong>, don&rsquo;t worry, it&rsquo;s temporary</li>
            </ul>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f959154b0cdf1cdf71ddef04e3787ef28462793e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=eec6c8bbb110dd7da91cdcec855da83f41eae5be66b4ea9e612d689c5c0bd5b9" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>5. More filters</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header, footer and a filters box.</p>
            <p>Layout: (based on&nbsp;<code>4-index.html</code>)</p>
            <ul>
                <li>Locations and Amenities filters:<ul>
                        <li>tag:&nbsp;<code>div</code></li>
                        <li>classname:&nbsp;<code>locations</code> for location tag and&nbsp;<code>amenities</code> for the other</li>
                        <li>inside the section filters (same level as the&nbsp;<code>button</code> Search)</li>
                        <li>height: 100% of the section filters</li>
                        <li>width: 25% of the section filters</li>
                        <li>border right #DDDDDD 1px only for the first left filter</li>
                        <li>contains a title:<ul>
                                <li>tag:&nbsp;<code>h3</code></li>
                                <li>font weight: 600</li>
                                <li>text&nbsp;<code>States</code> or&nbsp;<code>Amenities</code></li>
                            </ul>
                        </li>
                        <li>contains a subtitle:<ul>
                                <li>tag:&nbsp;<code>h4</code></li>
                                <li>font weight: 400</li>
                                <li>font size: 14px</li>
                                <li>text with fake contents</li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use:&nbsp;<code>header</code>,&nbsp;<code>footer</code>,&nbsp;<code>section</code>,&nbsp;<code>button</code>,&nbsp;<code>h3</code>,&nbsp;<code>h4</code> tags</li>
                <li>No inline style</li>
                <li>You are not allowed to use the&nbsp;<code>img</code> tag</li>
                <li>You are not allowed to use the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag</li>
                <li>All images must be stored in the&nbsp;<code>images</code> folder</li>
                <li>You must have 4 CSS files:<ul>
                        <li><code>styles/4-common.css</code>: for the global style (<code>body</code> and&nbsp;<code>.container</code> styles)</li>
                        <li><code>styles/3-header.css</code>: for the header style</li>
                        <li><code>styles/3-footer.css</code>: for the footer style</li>
                        <li><code>styles/5-filters.css</code>: for the filters style</li>
                    </ul>
                </li>
            </ul>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/85bfa50b96c2985723daa75b5e22f75ef16e2b2e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=463126fd2321c4ccaaa89c52a831dd60a003e5a4498778ee3d814c64ff4fd322" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>6. It&apos;s (h)over</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header, footer and a filters box with dropdown.</p>
            <p>Layout: (based on&nbsp;<code>5-index.html</code>)</p>
            <ul>
                <li>Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter&nbsp;<code>div</code>:<ul>
                        <li>tag&nbsp;<code>ul</code></li>
                        <li>classname&nbsp;<code>popover</code></li>
                        <li>text should be fake now</li>
                        <li>inside each&nbsp;<code>div</code></li>
                        <li>not displayed by default</li>
                        <li>color #FAFAFA</li>
                        <li>width same as the&nbsp;<code>div</code> filter</li>
                        <li>border #DDDDDD 1px with border radius 4px</li>
                        <li>no list display</li>
                        <li>Location filter has 2 levels of&nbsp;<code>ul</code>/<code>li</code>:<ul>
                                <li>state -&gt; cities</li>
                                <li>state name must be display in a&nbsp;<code>h2</code> tag (font size 16px)</li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use:&nbsp;<code>header</code>,&nbsp;<code>footer</code>,&nbsp;<code>section</code>,&nbsp;<code>button</code>,&nbsp;<code>h3</code>,&nbsp;<code>h4</code>,&nbsp;<code>ul</code>,&nbsp;<code>li</code> tags</li>
                <li>No inline style</li>
                <li>You are not allowed to use the&nbsp;<code>img</code> tag</li>
                <li>You are not allowed to use the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag</li>
                <li>All images must be stored in the&nbsp;<code>images</code> folder</li>
                <li>You must have 4 CSS files:<ul>
                        <li><code>styles/4-common.css</code>: for the global style (<code>body</code> and&nbsp;<code>.container</code> styles)</li>
                        <li><code>styles/3-header.css</code>: for the header style</li>
                        <li><code>styles/3-footer.css</code>: for the footer style</li>
                        <li><code>styles/6-filters.css</code>: for the filters style</li>
                    </ul>
                </li>
            </ul>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6262f13624dca23ca19db505c44f88faddb82ebb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0168cbe6fdc8279f2a83a950d65b7a7d23b5c13a7f91785835dca1fe96a750d6" alt="">&nbsp;<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6e6bdfa13fa88a5f439d9e2b1dade826dd95529b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cd57f20f9187c2c5ea27f6d98716fa858c242dc5e799ac6881e1bb08870c3872" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>7. Display results</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header, footer, a filters box with dropdown and results.</p>
            <p>Layout: (based on&nbsp;<code>6-index.html</code>)</p>
            <ul>
                <li>Add Places section:<ul>
                        <li>tag:&nbsp;<code>section</code></li>
                        <li>classname:&nbsp;<code>places</code></li>
                        <li>same level as the filters section, inside&nbsp;<code>.container</code></li>
                        <li>contains a title:<ul>
                                <li>tag:&nbsp;<code>h1</code></li>
                                <li>text:&nbsp;<code>Places</code></li>
                                <li>align in the top left</li>
                                <li>font size: 30px</li>
                            </ul>
                        </li>
                        <li>contains multiple &ldquo;Places&rdquo; as listing (horizontal or vertical) describe by:<ul>
                                <li>tag:&nbsp;<code>article</code></li>
                                <li>width: 390px</li>
                                <li>padding and margin 20px</li>
                                <li>border #FF5A5F 1px with radius 4px</li>
                                <li>contains the place name:<ul>
                                        <li>tag:&nbsp;<code>h2</code></li>
                                        <li>font size: 30px</li>
                                        <li>center horizontally</li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use:&nbsp;<code>header</code>,&nbsp;<code>footer</code>,&nbsp;<code>section</code>,&nbsp;<code>article</code>,&nbsp;<code>button</code>,&nbsp;<code>h1</code>,&nbsp;<code>h2</code>,&nbsp;<code>h3</code>,&nbsp;<code>h4</code>,&nbsp;<code>ul</code>,&nbsp;<code>li</code> tags</li>
                <li>No inline style</li>
                <li>You are not allowed to use the&nbsp;<code>img</code> tag</li>
                <li>You are not allowed to use the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag</li>
                <li>All images must be stored in the&nbsp;<code>images</code> folder</li>
                <li>You must have 5 CSS files:<ul>
                        <li><code>styles/4-common.css</code>: for the global style (i.e.&nbsp;<code>body</code> and&nbsp;<code>.container</code> styles)</li>
                        <li><code>styles/3-header.css</code>: for the header style</li>
                        <li><code>styles/3-footer.css</code>: for footer style</li>
                        <li><code>styles/6-filters.css</code>: for the filters style</li>
                        <li><code>styles/7-places.css</code>: for the places style</li>
                    </ul>
                </li>
            </ul>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/bca4d17fbe21a58b66a9d5d6b85df4801d147dd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8603dac2ee61be0e3c86a33dfe693b92c871c789267683c50b8e427b0ddc4d29" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>8. More details</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.</p>
            <p>Layout: (based on&nbsp;<code>7-index.html</code>)</p>
            <p>Add more information to a Place&nbsp;<code>article</code>:</p>
            <ul>
                <li>Price by night:<ul>
                        <li>tag:&nbsp;<code>div</code></li>
                        <li>classname:&nbsp;<code>price_by_night</code></li>
                        <li>same level as the place name</li>
                        <li>font color: #FF5A5F</li>
                        <li>border: #FF5A5F 4px rounded</li>
                        <li>min width: 60px</li>
                        <li>height: 60px</li>
                        <li>font size: 30px</li>
                        <li>align: the top right (with space)</li>
                    </ul>
                </li>
                <li>Information section:<ul>
                        <li>tag:&nbsp;<code>div</code></li>
                        <li>classname:&nbsp;<code>information</code></li>
                        <li>height: 80px</li>
                        <li>border: top and bottom #DDDDDD 1px</li>
                        <li>contains (align vertically):<ul>
                                <li>Number of guests:<ul>
                                        <li>tag:&nbsp;<code>div</code></li>
                                        <li>classname:&nbsp;<code>max_guest</code></li>
                                        <li>width: 100px</li>
                                        <li>fake text</li>
                                        <li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_group.png" title="icon" target="_blank">icon</a></li>
                                    </ul>
                                </li>
                                <li>Number of bedrooms:<ul>
                                        <li>tag:&nbsp;<code>div</code></li>
                                        <li>classname:&nbsp;<code>number_rooms</code></li>
                                        <li>width: 100px</li>
                                        <li>fake text</li>
                                        <li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bed.png" title="icon" target="_blank">icon</a></li>
                                    </ul>
                                </li>
                                <li>Number of bathrooms:<ul>
                                        <li>tag:&nbsp;<code>div</code></li>
                                        <li>classname:&nbsp;<code>number_bathrooms</code></li>
                                        <li>width: 100px</li>
                                        <li>fake text</li>
                                        <li><a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bath.png" title="icon" target="_blank">icon</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>User section:<ul>
                        <li>tag:&nbsp;<code>div</code></li>
                        <li>classname:&nbsp;<code>user</code></li>
                        <li>text&nbsp;<code>Owner: &lt;fake text&gt;</code></li>
                        <li><code>Owner</code> text should be in bold</li>
                    </ul>
                </li>
                <li>Description section:<ul>
                        <li>tag:&nbsp;<code>div</code></li>
                        <li>classname:&nbsp;<code>description</code></li>
                    </ul>
                </li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use:&nbsp;<code>header</code>,&nbsp;<code>footer</code>,&nbsp;<code>section</code>,&nbsp;<code>article</code>,&nbsp;<code>button</code>,&nbsp;<code>h1</code>,&nbsp;<code>h2</code>,&nbsp;<code>h3</code>,&nbsp;<code>h4</code>,&nbsp;<code>ul</code>,&nbsp;<code>li</code> tags</li>
                <li>No inline style</li>
                <li>You are not allowed to use the&nbsp;<code>img</code> tag</li>
                <li>You are not allowed to use the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag</li>
                <li>All images must be stored in the&nbsp;<code>images</code> folder</li>
                <li>You must have 5 CSS files:<ul>
                        <li><code>styles/4-common.css</code>: for the global style (i.e.&nbsp;<code>body</code> and&nbsp;<code>.container</code> styles)</li>
                        <li><code>styles/3-header.css</code>: for the header style</li>
                        <li><code>styles/3-footer.css</code>: for the footer style</li>
                        <li><code>styles/6-filters.css</code>: for the filters style</li>
                        <li><code>styles/8-places.css</code>: for the places style</li>
                    </ul>
                </li>
            </ul>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f4b2d4ef94bd3a2e7e1ddefa81236595686d270e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b12284f1fba03daacd44e1b77e0c477510d019272eee3b50d2929e52b6964801" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>9. Full details</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Write an HTML page that displays a header, footer, a filters box with dropdown and results.</p>
            <p>Layout: (based on&nbsp;<code>8-index.html</code>)</p>
            <p>Add more information to a Place&nbsp;<code>article</code>:</p>
            <ul>
                <li>List of Amenities:<ul>
                        <li>tag&nbsp;<code>div</code></li>
                        <li>classname&nbsp;<code>amenities</code></li>
                        <li>margin top 40px</li>
                        <li>contains:<ul>
                                <li>title:<ul>
                                        <li>tag&nbsp;<code>h2</code></li>
                                        <li>text&nbsp;<code>Amenities</code></li>
                                        <li>font size 16px</li>
                                        <li>border bottom #DDDDDD 1px</li>
                                    </ul>
                                </li>
                                <li>list of amenities:<ul>
                                        <li>tag&nbsp;<code>ul</code> /&nbsp;<code>li</code></li>
                                        <li>no list style</li>
                                        <li>icons on the left:&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_pets.png" title="Pet friendly" target="_blank">Pet friendly</a>,&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_tv.png" title="TV" target="_blank">TV</a>,&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_wifi.png" title="Wifi" target="_blank">Wifi</a>, etc&hellip; feel free to add more</li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>List of Reviews:<ul>
                        <li>tag&nbsp;<code>div</code></li>
                        <li>classname&nbsp;<code>reviews</code></li>
                        <li>margin top 40px</li>
                        <li>contains:<ul>
                                <li>title:<ul>
                                        <li>tag&nbsp;<code>h2</code></li>
                                        <li>text&nbsp;<code>Reviews</code></li>
                                        <li>font size 16px</li>
                                        <li>border bottom #DDDDDD 1px</li>
                                    </ul>
                                </li>
                                <li>list of review:<ul>
                                        <li>tag&nbsp;<code>ul</code> /&nbsp;<code>li</code></li>
                                        <li>no list style</li>
                                        <li>a review is described by:<ul>
                                                <li><code>h3</code> tag for the user/date description (font size 14px). Ex: &ldquo;From Bob Dylan the 27th January 2017&rdquo;</li>
                                                <li><code>p</code> tag for the text (font size 12px)</li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <p>Requirements:</p>
            <ul>
                <li>You must use:&nbsp;<code>header</code>,&nbsp;<code>footer</code>,&nbsp;<code>section</code>,&nbsp;<code>article</code>,&nbsp;<code>button</code>,&nbsp;<code>h1</code>,&nbsp;<code>h2</code>,&nbsp;<code>h3</code>,&nbsp;<code>h4</code>,&nbsp;<code>ul</code>,&nbsp;<code>li</code> tags</li>
                <li>No inline style</li>
                <li>You are not allowed to use the&nbsp;<code>img</code> tag</li>
                <li>You are not allowed to use the&nbsp;<code>style</code> tag in the&nbsp;<code>head</code> tag</li>
                <li>All images must be stored in the&nbsp;<code>images</code> folder</li>
                <li>You must have 5 CSS files:<ul>
                        <li><code>styles/4-common.css</code>: for the global style (<code>body</code> and&nbsp;<code>.container</code> styles)</li>
                        <li><code>styles/3-header.css</code>: for the header style</li>
                        <li><code>styles/3-footer.css</code>: for the footer style</li>
                        <li><code>styles/6-filters.css</code>: for the filters style</li>
                        <li><code>styles/100-places.css</code>: for the places style</li>
                    </ul>
                </li>
            </ul>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f54486a431a05ea3477e337e0e953686d3c6ffd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230522%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230522T202220Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=45986e0d203c9e1b18c8ac1e6ef2dc864e86038aff55076c9a83859e8aa72b7d" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>100-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/100-places.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>10. Flex</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Improve the Places section by using&nbsp;<a href="https://intranet.alxswe.com/rltoken/Xc-nBlQHexwNaCuKYpZ2-A" title="Flexible boxes" target="_blank">Flexible boxes</a> for all Place articles</p>
            <p><a href="https://intranet.alxswe.com/rltoken/PZz46Gkdj5Mo9-AWERPhQA" title="Flexbox Froggy" target="_blank">Flexbox Froggy</a></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>101-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/101-places.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>11. Responsive design</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Improve the page by adding&nbsp;<a href="https://intranet.alxswe.com/rltoken/9mRhZcLRxmsuCyF8q7S8Ww" title="responsive design" target="_blank">responsive design</a> to display correctly in mobile or small screens.</p>
            <p>Examples:</p>
            <ul>
                <li>no horizontal scrolling</li>
                <li>redesign search bar depending of the width</li>
                <li>etc.</li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>102-index.html, styles/102-common.css, styles/102-header.css, styles/102-footer.css, styles/102-filters.css, styles/102-places.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>12. Accessibility</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Improve the page by adding&nbsp;<a href="https://intranet.alxswe.com/rltoken/JO-zonPvzBUfqpYRZDAtug" title="Accessibility support" target="_blank">Accessibility support</a></p>
            <p>Examples:</p>
            <ul>
                <li>Colors contrast</li>
                <li>Header tags</li>
                <li>etc.</li>
            </ul>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone</code></li>
                    <li>Directory:&nbsp;<code>web_static</code></li>
                    <li>File:&nbsp;<code>103-index.html, styles/103-common.css, styles/103-header.css, styles/103-footer.css, styles/103-filters.css, styles/103-places.css, images/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>