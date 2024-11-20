using Dapr.Client;
using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using System.Text.Json;


namespace DaprDemo.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class SampleController : ControllerBase
    {
        private readonly DaprClient _daprClient;

        public SampleController(DaprClient daprClient)
        {
            _daprClient = daprClient;
        }

        [HttpGet("invoke")]
        public async Task<IActionResult> InvokeMethod()
        {
            var result = await _daprClient.InvokeMethodAsync<int>(HttpMethod.Get, "stateapi", "get");
            return Ok(result);
        }


        [HttpPost("set")]
        public async Task<IActionResult> SetNumber([FromBody] JsonElement body)
        {
            if (body.TryGetProperty("number", out JsonElement numberElement) && numberElement.TryGetInt32(out int number))
            {
                var data = new { number = number };
                await _daprClient.InvokeMethodAsync(HttpMethod.Post, "stateapi", "set", data);
                return Ok();
            }
            return BadRequest("Invalid JSON payload");
        }

    }
}