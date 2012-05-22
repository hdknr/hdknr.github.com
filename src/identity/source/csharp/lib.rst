.. code-block:: csharp

    // Micsosoft
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    using System.Text.RegularExpressions;
    using System.IO;
    using System.Security.Cryptography;
    
    // BouncyCastle
    using Org.BouncyCastle.OpenSsl;
    using Org.BouncyCastle.Crypto;
    using Org.BouncyCastle.Crypto.Signers;
    using Org.BouncyCastle.Crypto.Digests;
    using Org.BouncyCastle.Crypto.Generators;
    using Org.BouncyCastle.Crypto.Parameters;
    using Org.BouncyCastle.X509;
    using Org.BouncyCastle.Security;
    
    // Json.NET
    using Newtonsoft.Json;
    using Newtonsoft.Json.Linq;
