using System;
using System.Linq;
using System.Reflection;
using ClosedXML.Excel;

foreach (var p in typeof(XLColor).GetProperties(BindingFlags.Public | BindingFlags.Instance))
    Console.WriteLine($"PROP {p.Name} {p.PropertyType.FullName}");
foreach (var m in typeof(XLColor).GetMethods(BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static).Where(m => m.Name.Contains("Theme") || m.Name.Contains("Color") || m.Name.Contains("Argb")))
    Console.WriteLine($"METH {m}");
