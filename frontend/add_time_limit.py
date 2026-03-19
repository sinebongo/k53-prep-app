import re

index_path = r"c:\Users\kings\AppData\Roaming\Microsoft\Windows\Libraries\Downloads\K53PrepApp\K53PrepApp\frontend\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

replacement = """      <div class="action-card bg-white border border-gray-100 rounded-custom shadow-sm hover:border-primary group w-full overflow-hidden">
        <button onclick="startTestWithDuration()" class="flex items-center p-6 text-left w-full">
          <div class="flex-shrink-0 p-3 bg-red-50 text-primary rounded-custom group-hover:bg-primary group-hover:text-white transition-colors">
            <svg class="h-8 w-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <div class="ml-5">
            <h2 class="text-xl font-bold text-gray-900">Take Practice Test</h2>
            <p class="text-gray-500 text-sm">Challenge yourself with a timed 64-question mock exam.</p>
          </div>
        </button>
        <div class="px-6 py-3 bg-gray-50 border-t border-gray-100 flex items-center justify-between">
          <label for="test-duration" class="text-sm font-semibold text-gray-700">Test Duration (Minutes):</label>
          <input type="number" id="test-duration" min="30" value="58" class="w-20 px-2 py-1 border border-gray-300 rounded-custom text-sm focus:ring-primary focus:border-primary">
        </div>
      </div>"""

# Replace the button block
pattern = re.compile(r'<button onclick="go\(\'test\'\)".*?</button>', re.DOTALL)
idx_content = pattern.sub(replacement, idx_content)

# Add startTestWithDuration function
script_add = """async function startTestWithDuration() {
  const durationInput = document.getElementById('test-duration');
  let duration = parseInt(durationInput.value);
  if (isNaN(duration) || duration < 30) {
    alert("Minimum test duration is 30 minutes.");
    durationInput.value = 30;
    return;
  }
  sessionStorage.setItem('testDuration', duration);
  go('test');
}"""

idx_content = idx_content.replace("async function go(destination) {", script_add + "\n\nasync function go(destination) {")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)

test_path = r"c:\Users\kings\AppData\Roaming\Microsoft\Windows\Libraries\Downloads\K53PrepApp\K53PrepApp\frontend\test.html"
with open(test_path, "r", encoding="utf-8") as f:
    test_content = f.read()

test_content = test_content.replace(
    "let secondsLeft = 58 * 60;", 
    "let storedDuration = parseInt(sessionStorage.getItem('testDuration')) || 58;\nlet secondsLeft = storedDuration * 60;"
)
# Update timer display default visually
test_content = test_content.replace('<span id="timer-display" class="font-mono text-lg font-bold text-red-600">58:00</span>', '<span id="timer-display" class="font-mono text-lg font-bold text-red-600">--:--</span>')

with open(test_path, "w", encoding="utf-8") as f:
    f.write(test_content)

print("Test duration functionality added.")
